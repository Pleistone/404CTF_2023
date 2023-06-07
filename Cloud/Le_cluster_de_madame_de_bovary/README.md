# Le Cluster de Madame Bovary

## Enoncé
Un individu dans un coin vous interpelle et vous invite à sa table. Une fois assis, il vous explique qu'il veut que vous infiltriez le cluster Kubernetes de Madame Bovary. Madame Bovary est une femme riche et influente qui a investi dans la technologie Kubernetes pour gérer les applications de son entreprise de production de médicaments. Vous vous doutez qu'il s'agit sans doute d'un concurrent industriel mais il vous offre une belle récompense si vous réalisez sa demande.

Votre mission consiste à prendre le contrôle du cluster Kubernetes de Madame Bovary et à accéder à ses applications critiques. Vous devrez exploiter toutes les vulnérabilités possibles pour atteindre votre objectif.

Le fichier fourni est une machine virtuelle à charger dans Virtualbox. Cette machine virtuelle contient le cluster Kubernetes du challenge.

> Utilisateur : ctf

> Mot de passe : 404ctf2023


## Solution

Après lecture de l'énoncé, il est clair que l'on doit extraire des informations contenues dans le cluster Kubernetes. À noter qu'un cluster est un ensemble de noeuds (machines virtuelles ou physiques) interconnectés qui exécutent des applications conteneurisées. Sur chaque noeud on trouve des groupes d'un ou plusieurs conteneurs qui sont gérés et exécutés ensemble, ces groupes sont appelés pod. De plus le nom "cluster Kubernetes" nous fait comprendre que l'on va probablement avoir à faire un cluster de type Kubernetes. 

1. Pour commencer, on procède au déploiement de la machine virtuelle à l'aide de Virtualbox. Ensuite, on débute nos recherches en listant les pods disponibles. Pour faire cela, on ouvre un terminal sur la machine virtuelle et on exécute la commande `kubectl get pods`. Cette opération nous fournit les informations suivantes :

```
$ kubectl get pods
NAME    READY   STATUS    RESTARTS        AGE
agent   1/1     Running   2 (3m13s ago)   48d
```

2. On trouve un seul pod, qui porte le nom "agent". Pour mieux comprendre ce qui s'exécute sur ce pod, examinons ses logs.

```
$ kubectl logs agent
Please deploy container 404ctf/the-container
```

3. Les logs nous indiquent qu'il faut déployer le conteneur pour accéder à plus d'information.

```
$ kubectl create deployment the-container --image=404ctf/the-container
deployment.apps/the-container created

$ kubectl get pods
NAME                            READY   STATUS    RESTARTS        AGE
agent                           1/1     Running   2 (3m25s ago)   48d
the-container-64f84f898-pwmr6   1/1     Running   0               46s
``` 

4. On regarde les logs du conteneur que l'on vient de déployer.

```
$ kubectl logs the-container-64f84f898-pwmr6
err: not in namespace 404ctf
```

5. On remarque qu'il y a une erreur sur le conteneur que l'on a déployé pour la résoudre, il faut redéployer le conteneur dans le namespace "404ctf". On crée donc le namespace "404ctf".
Puis on reprend à partir de l'étape 3, mais on ajoute l'option `--namespace=404ctf`.

```
$ kubectl create namespace 404ctf
namespace/404ctf created

$ kubectl create deployment the-container-2 --image=404ctf/the-container --namespace=404ctf
deployment.apps/the-container-2 created

$ kubectl get pods --namespace=404ctf
NAME                               READY   STATUS    RESTARTS        AGE
the-container-2-6c58674555-7zq8r   1/1     Running   0               32s
``` 

6. On regarde les logs du conteneur que l'on vient de déployer.

```
$ kubectl logs the-container-2-6c58674555-7zq8r
err: /opt/my_secret_dir/ does not exist
```

7. On a encore une erreur, mais il semble que le conteneur ait été déployé correctement. De plus le fichier dossier opt de ce conteneur semble pouvoir contenir des informations intéressantes. On va donc accéder au conteneur et regarder si le dossier opt ne contiendrait pas le flag.

```
$ kubectl exec -it the-container-2-6c58674555-7zq8r --namespace=404ctf -- sh
/ # strings /opt/the-container | grep -A 20 '404CTF{'
  404CTF{A_la_decouv le reste du flag est dans le container 404ctf/web-server
```

8. On a donc trouvé la première moitié du flag et on apprend donc que le reste du flag se trouve dans le conteneur web-server.
On réaliser donc les mêmes étapes que précédemment pour le déployer.

```
$ kubectl create deployment web-server --image=404ctf/web-server
deployment.apps/web-server created

$ kubectl get pods
NAME                               READY   STATUS    RESTARTS         AGE
agent                              1/1     Running   2 (10m25s ago)   48d
the-container-64f84f898-pwmr6      1/1     Running   0                7min46s
web-server-8465698799-kz7sj        1/1     Running   0                22s

$ kubectl logs web-server-8465698799-kz7sj
Starting serveur at port 8080

$ kubectl exec -it web-server-8465698799-kz7sj -- sh
#
```

9. On sait que la suite du flag se trouve sur ce serveur et les logs du pod nous indique que le serveur web est accessible sur le port 8080. On va donc aller voir ce qu'il un a sur ce port en redirigeant le port 8080 du pod web-serveur vers notre port 8080.

```
$ kubectl port-forward pod/web-server-8465698799-kz7sj  8080:8080
Forwarding from 127.0.0.1:8080 -> 8080
Forwarding [::1]:8080 -> 8080
```

10. On peut désormais faire une requête sur l'url `http://localhost:8080` a l'aide Curl ou d'un navigateur. On arrive sur une page web sur la quel se trouve le message "Le drapeau est dans /flag". On vas donc sur la page `http://localhost:8080/flag` et la on trouve la fin du flag qui est "erte_de_k8s}".

<p align="center"><img src="la fin du flag.png" alt="La fin du flag" width="750"></p>

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{A_la_decouverte_de_k8s}
```
