import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import cv2


def get_number(image):
    model = Sequential()
    input_shape=(28,28,1)
    num_classes=10
    model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=input_shape))
    model.add(Conv2D(64, (3,3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    model.load_weights('mnist_model.h5')
    model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta())
    im_pred = list(model.predict(image)[0])
    max_value = max(im_pred)
    output = im_pred.index(max_value)
    return output


#Recupérer les chiffres
n1=0
n2=6535
number_list = []
for i in range(n1,n2):
    print("Image :",i)
    image = 'images/'+str(i)+'.jpg'
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    image = image.reshape(1,28,28,1)
 
    number = get_number(image)
    number_list.append(number)


#Transformer en binaire
bin_str = ""
def pariter(number):
    return number%2

for i in number_list:
    bin_str+=str(pariter(i))


#Transformer en ascii
byte_segments = [int(bin_str[i:i+8],2) for i in range(0, len(bin_str), 8)]
ascii_string = ''.join([chr(segment) for segment in byte_segments])
print(ascii_string)