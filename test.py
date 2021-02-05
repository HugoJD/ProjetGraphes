import fileinput
from collections import defaultdict, Counter
import networkx as nx

#Commande pour importer le fichier contenant le graphe dans la console:
#cat .\komu.gr | python .\test.py

"""
On veut ajouter ou retirer le moin d'arêtes possible dans un graphe afin que tous les ensembles du graphe soient des cliques.
L'idée est de comparer les voisins de chaque sommet pour voir ce qui ont le plus de voisins en commun. 

Ebauche de solution:
Parcourir le graphe pour savoir si des cliques existent déjà.
Si oui, faire en sorte de ne plus les prendre en compte. Cela permet de réduire la taille du graphe à manipuler.
Dans un graphe, trouver les CC et identifier une coupe min. Supprimer les arêtes de cette coupe. Et pour chaque CC créée,
ajouter les arêtes manquantes.

Autre solution:
On liste les voisins de chaque sommet. 
On compare chaque liste pour connaitre les sommets en commun de listes deux à deux.
Si les deux listes ont la même taille, alors elles ont 100% de leurs voisins en commun (avec & de la structure de données des set)

"""

#On crée une liste de vide d'arêtes pour y mettre celle du fichier en entrée:
Aretes=[]

for line in fileinput.input():
    if line[0].isdigit():
        line=line.split()
        Aretes.append((int(line[0]),int(line[1])))

fileinput.close()

Aretes=sorted(Aretes)

G = nx.Graph()
G.add_edges_from(Aretes)
print(list(nx.enumerate_all_cliques(G)))

#On crée un graphe (qui sera un set) à partir de la liste des arêtes
def CreerGraphe(Aretes):
    Graph=defaultdict(set)
    for node1, node2 in Aretes:
        Graph[node1].add(node2)
        Graph[node2].add(node1)
    return Graph

"""
L’heuristique gloutonne utilisée consiste à choisir à chaque itération le sommet ayant le
plus grand nombre de voisins dans l’ensemble cand de tous les sommets pouvant être ajoutés à la clique c en cours
de construction.
Fonction chercheCliqueGlouton(g)
Entrée : Un graphe g = (S, A)
Postcondition : retourne une clique de g
2 cand ← S
3 c ← ∅
4 tant que cand 6= ∅ faire
5 Soit si
le sommet de cand maximisant |cand ∩ adj(si)|
6 c ← c ∪ {si}
7 cand ← cand ∩ adj(si)
8 retourne c
"""

def GetDegreDeConnexionNode(Graphe,node):
    voisins=set(Graphe[node])
    print("Voisins :", voisins)
    nbrVoisin=float(len(voisins))
    ListeDegre=[]
    for v in voisins:
        voisins_2nd=set(Graphe[int(v)])
        print("Voisins_2nd :",voisins_2nd)
        degSommet=float(len(voisins & voisins_2nd)+1)
        ListeDegre.append((degSommet/nbrVoisin))
    return ListeDegre


def FormeUneClique(Graphe,node):
    voisins=set(Graph[node])
    nbrVoisin=float(len(voisins))
    for v in voisins:
        voisins_2nd=set(Graph[int(v)])
        degSommet=float(len(voisins & voisins_2nd)+1)
        if degSommet/nbrVoisin<1:
            return False
    return True


"""
for node in Graph:
    voisin=set(Graph[node])
    nbrVoisin=len(node)
    k=0
    for nodeVoisin in voisin: #pour chaque voisin de notre sommet exploré

    #regarder nombre de node voisin commun --> incrémenter k=k+1
        if (k/nbrVoisin>=nbrVoisin-nbrarrêtemanquantes):
            #ici faire un ajout


if (k/nbrvoisin>=nbrvoisin-nbrarrêtemanquantes):
le critère est là
tu incrémentes k à chaque fois que tu as une redondance de sommet chez le voisin,
et donc tu sais si le voisin est connecté aux mêmes sommets.
"""

print(Aretes[0][0])

Graphe = CreerGraphe(Aretes)
print(Aretes)
print(Graphe)
print("type :", type(Graphe))
for i in Graphe:
    print(i, "a pour voisins : ",Graphe[i])


for node in Graphe:
    print("Noeud : ", node)
    sommet=set(Graphe[node])
    print("sommetsVoisins : ",sommet)
    for voisin in sommet:
        print("voisin : ", voisin)
        voisinsVoisin=set(Graphe[voisin])
        print("VoisinsVoisins : ", voisinsVoisin)
        print("Voisins en commun avec ", node, " : ",sommet & voisinsVoisin)

print("Get degre de connexion noeud : \n", GetDegreDeConnexionNode(Graphe, 1))

G = [
        [ 0 , 1 , 1 ] ,
        [ 1 , 0 , 1 ] ,
        [ 1 , 1 , 0 ]
    ]

