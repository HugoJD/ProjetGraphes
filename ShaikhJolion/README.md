README.md

Le programme "ShaikhJolion" est un programme implémenté dans le langage Python.
Il permet de créer une union de cliques à partir d'un graphe non orienté.

L'exécution du programme se fait grâce à la commande suivante : 
cat file.gr | python3 ShaikhJolion.py > solution 

Le fichier envoyé au programme répond à un format précis.
Les lignes du fichier en entrée n'ayant que deux chiffres indiquent une arête en particulier où chaque chiffre correspond à un sommet. Les sommets sont séparés par un espace.
Voici un exemple de format:

c This file describes a path with five vertices and four edges.
p cep 5 4
1 2
2 3
c we are half-way done with the instance definition.
3 4
4 5

Dans cet exemple, le sommet 1 est relié au sommet 2, le sommet 3 est relié au sommet 3, etc...

Enfin, le fichier renvoyé à la fin du programme ("solution") contiendra toutes les éditions d'arêtes qui ont été nécessaires pour créer une union de cliques à partir du graphe initiale.
Les éditions d'arêtes sont aussi bien des ajouts que des suppressions d'arêtes.
Le format de sortie des arêtes est celui-ci:

1 2
2 3
3 4
4 1
