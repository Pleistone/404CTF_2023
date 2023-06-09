import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications.resnet50 import ResNet50


# chargement du resnet50
model = ResNet50(weights='imagenet')

def load_image_tf(img_path):
    image_raw = tf.io.read_file(img_path)
    image = tf.image.decode_image(image_raw)
    return image

def save_image_tf32(image_tensor, filepath):
    image_tensor = tf.cast(image_tensor, tf.uint8)
    image_raw = tf.image.encode_png(image_tensor)
    tf.io.write_file(filepath, image_raw)


def create_adversarial_noise(input_image, input_label, model, max_change=55):
    # ajustement des dimensions
    input_image = tf.expand_dims(input_image, 0)

    # loss et gradient
    loss_object = tf.keras.losses.CategoricalCrossentropy()
    gradient_fn = tf.keras.optimizers.schedules.PolynomialDecay(
        initial_learning_rate=0.1,
        decay_steps=10000,
        end_learning_rate=0.01
    )
    
    perturbations = tf.zeros_like(input_image)

    for i in range(30):  # Gradient descent steps
        with tf.GradientTape() as tape:
            tape.watch(perturbations)
            adversarial_img = input_image + perturbations
            prediction = model(adversarial_img)
            loss = loss_object(input_label, prediction)

        # suivi du gradient pour se rapprocher de la cible
        gradients = tape.gradient(loss, perturbations)
        perturbations -= gradient_fn(i) * tf.sign(gradients)
        
        # Clip pour rester raisonnable
        perturbations = tf.clip_by_value(perturbations, -max_change, max_change)

        if loss.numpy()<0.000000001:
            print(f"Iteration {i}, loss: {loss}")
            print(f"Predicted class: {np.argmax(prediction)}")
            break

        if i % 10 == 0:
            print(f"Iteration {i}, loss: {loss}")
            print(f"Predicted class: {np.argmax(prediction)}")

    return perturbations



def build_noise(input_image, target_class=849):
    # creation de la cible 413
    target_label = tf.one_hot(target_class, 1000)
    target_label = tf.reshape(target_label, (1, 1000))

    # creation du bruitage
    adversarial_noise = create_adversarial_noise(input_image, target_label, model)

    # adaptation de taille de tensor
    adversarial_noise = tf.squeeze(adversarial_noise, 0)
    return adversarial_noise


def apply_adversarial_changes32(original_image, adversarial_noise):
    original_image = tf.cast(original_image, tf.float32)
    adversarial_image = original_image + adversarial_noise
    # a priori, pas utile, mais on sait jamais
    adversarial_image = tf.clip_by_value(adversarial_image, 0, 255)
    return adversarial_image


def main():
    # chargement de l'image de reference
    file = "chat.jpg"
    original_image = load_image_tf(file)

    # creation de l'image de travail
    image = tf.cast(original_image, tf.float32)
    image = tf.image.resize(image, (224, 224))
    image = tf.keras.applications.resnet50.preprocess_input(image)

    # fabrication du bruitage
    adversarial_noise = build_noise(image)

    # et application a l'image
    adversarial_image32 = apply_adversarial_changes32(original_image, adversarial_noise)

    # sauvegarde pour exploitation
    adversarial_file = "solution 1.png"
    save_image_tf32(adversarial_image32, adversarial_file)

    print(f"image => {adversarial_file}")

main()
