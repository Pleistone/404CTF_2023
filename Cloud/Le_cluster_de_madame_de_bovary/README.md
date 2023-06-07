# Le Cluster de Madame Bovary

## Enoncé
Un individu dans un coin vous interpelle et vous invite à sa table. Une fois assis, il vous explique qu'il veut que vous infiltriez le cluster Kubernetes de Madame Bovary. Madame Bovary est une femme riche et influente qui a investi dans la technologie Kubernetes pour gérer les applications de son entreprise de production de médicaments. Vous vous doutez qu'il s'agit sans doute d'un concurrent industriel mais il vous offre une belle récompense si vous réalisez sa demande.

Votre mission consiste à prendre le contrôle du cluster Kubernetes de Madame Bovary et à accéder à ses applications critiques. Vous devrez exploiter toutes les vulnérabilités possibles pour atteindre votre objectif.

Le fichier fourni est une machine virtuelle à charger dans Virtualbox. Cette machine virtuelle contient le cluster Kubernetes du challenge.

> Utilisateur : ctf

> Mot de passe : 404ctf2023


## Solution

Après lecture de l'énoncé, il est clair que l'on doit extraire des informations contenues dans le cluster Kubernetes. À noter qu'un cluster est un ensemble de noeuds (machines virtuelles ou physiques) interconnectés qui exécutent des applications conteneurisées. Sur chaque noeud on trouve des groupes d'un ou plusieurs conteneurs qui sont gérés et exécutés ensemble, ces groupes sont appelés pod. De plus le nom "cluster Kubernetes" nous fait comprendre que l'on va probablement avoir à faire un cluster de type Kubernetes. 

On déploie donc la machine virtuelle avec Virtualbox, puis on commence par lister les pods disponibles. Pour ce faire, on ouvre un terminal sur la machine virtuelle et exécute la commande `kubectl get pods`, ce qui nous donne les informations suivantes :

```
$ kubectl get pods
```




## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{A_la_decouverte_de_k8s}
```
