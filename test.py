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

import fileinput
import time
from collections import defaultdict, Counter

# debut = time.perf_counter()

#On crée une liste vide d'arêtes pour y mettre celles du fichier en entrée:
Liste_aretes=[]

for line in fileinput.input():
    if line[0].isdigit():
        line=line.split()
        Liste_aretes.append((int(line[0]),int(line[1])))

fileinput.close()

Liste_aretes=sorted(Liste_aretes)
# print("Taille liste des arêtes: ", len(Liste_aretes))

# lecture_file = time.perf_counter()
# print(f"Lecture du fichier en {lecture_file - debut:0.2f} secondes")

#On créer un graphe à partir de la liste d'arêtes:
def CreerGraphe(Liste_aretes):
    Graphe = defaultdict(list)
    for u, v in Liste_aretes:
        Graphe[u].append(v)
        Graphe[v].append(u)
    return Graphe


#On veut récupérer le sommet ayant le plus de voisins
#On itère sur chaque voisin pour voir s'il a lui aussi des arêtes avec les autres voisins du sommet initial.
#Si non, on ajoute l'arête manquante. Et on supprime les arêtes qui vont vers d'autres sommets que les voisins du sommet initial.

#Fonction pour supprimer une arête du graphe
#On parcourt les voisins des sommets et on supprimer le sommet correspondant.
#On utilise del plutôt que pop() car plus rapide
def supprimerArete(Graphe, u,v):
    #print(Graphe)
    # print("u = ", u)
    # print("v = ", v)
    i = 0
    while i < len(Graphe[u]):
    # for i in range(0,len(Graphe[u])):
        # print("len de u",len(Graphe[u]))
        # print("i = ",i)
        # print("Voisins de ", u, ":",Graphe[u])
        # print("Voisin comparé de u", Graphe[u][i])
        if Graphe[u][i] == v:
            #print("suppression ",Graphe[u][i],u)
            del Graphe[u][i]
        i+=1
    j = 0
    while j < len(Graphe[v]):
    # for j in range(0,len(Graphe[v])):
        # print("len de v",len(Graphe[v]))
        # print("j = ",j)
        # print("Voisins de ", v, ":",Graphe[v])
        # print("Voisin comparé de v", Graphe[v][j])
        if Graphe[v][j] == u:
            #print("suppression ",Graphe[v][j], v)
            del Graphe[v][j]
        j+=1
    return Graphe


def ajoutArete(Graphe, u, v):
    if v not in Graphe[u]:
        #print("Ajout : (",u,v,")")
        Graphe[u].append(v)
    if u not in Graphe[v]:
        #print("Ajout : (",v,u,")")
        Graphe[v].append(u)
    return Graphe

#Fonction pour avoir le sommet avec le plus grand degré:
def DegreSommet(Graphe):
    ListeDegre = {}
    for i in Graphe:
        ListeDegre[i] = len(Graphe[i])
    return ListeDegre

def degreMax(ListeDegre):
    value = list(ListeDegre.values())
    key = list(ListeDegre.keys())
    return key[value.index(max(value))]


def creerClique(Graphe, u, ListeEdition, Explore):
    Explore.append(u)
    A_Supprimer = []
    for v in Graphe[u]:#on regarde chaque voisin de u
        #print("Graphe = ", Graphe)
        Explore.append(v)
        for w in Graphe[u]:#pour un voisin de u, on regarde si w n'est pas déjà un voisin de v, si non, on ajoute l'arête
            if w not in Graphe[v] and w != v:
                Graphe = ajoutArete(Graphe, w, v)
                ListeEdition.append((w,v))
        for w in Graphe[v]:#pour un voisin de v, s'il n'est pas voisin de u, on le supprime de v
            if w not in Graphe[u] and w != u:
                A_Supprimer.append((w,v))
                # Graphe = supprimerArete(Graphe, w, v)
                ListeEdition.append((w,v))
                #print("A supprimer: ",A_Supprimer)
    for w in A_Supprimer:
        Graphe = supprimerArete(Graphe, w[0], w[1])
        #print(Graphe)
    return Graphe, ListeEdition, Explore

# Graphe sans les sommets dans Explore
def grapheSansClique(Graphe, ListeEdition, Explore):
    for i in Explore:
        if Graphe[i] not in Explore:
            Graphe.pop(i)
    #print("Nouveau graphe sans clique ", Graphe)
    return Graphe, ListeEdition, Explore

def UnionClique(Graphe):
    ListeEdition = []
    Explore = []
    # ListeDegre = {}
    maxi = None
    while len(Graphe) != 0:
        # ListeDegre = DegreSommet(Graphe)
        maxi = max(Graphe, key=Graphe.get)
        # print("degré maxi = ", maxi)
        # maxi = degreMax(ListeDegre)
        Graphe, ListeEdition, Explore = creerClique(Graphe, maxi, ListeEdition, Explore)
        Graphe, ListeEdition, Explore = grapheSansClique(Graphe, ListeEdition, Explore)
    print("Graphe : ", Graphe)
    print("ListeEdition ", ListeEdition)
    print("Explore ", Explore)
    return Graphe, ListeEdition, Explore


# Graphe = CreerGraphe(Liste_aretes)
# print("Graphe = ", Graphe)
# print("Ajout arête (2,5)")
# Graphe = ajoutArete(Graphe, 2, 5)
# print("Graphe après ajout = ", Graphe)
# print("Suppression arête (5,4)")
# Graphe = supprimerArete(Graphe, 5, 4)
# print("Graphe après suppression = ", Graphe)
# print("Suppression arête (1,2)")
# Graphe = supprimerArete(Graphe, 1, 2)
# print("Graphe après suppression ", Graphe)
# print("Ajout arête (1,5)")
# Graphe = ajoutArete(Graphe, 1,5)
# print("Graphe après ajout : ", Graphe)
# ListeDegre = DegreSommet(Graphe)
# print("Liste degrés = ", ListeDegre)
# print("Sommet avec plus grand degré : ", degreMax(ListeDegre))
# degreMax = degreMax(ListeDegre)
# Graphe, ListeEdition, Explore = creerClique(Graphe, degreMax)
# print("Clique avec voisins de", degreMax," : ", Graphe)
# print("Explore : ", Explore)
# print("Liste Edition : ", ListeEdition)
# tic = time.perf_counter()
Graphe = CreerGraphe(Liste_aretes)
# Graphe, ListeEdition, Explore = UnionClique(Graphe)
print("Graphe = ", Graphe)
# toc = time.perf_counter()
# print(f"Création du graphe en {toc - tic:0.2f} secondes")
print("Taille Graphe = ", len(Graphe))
# tic_algo = time.perf_counter()
ListeEdition = []
Explore = []
ListeDegre = {}
maxi = None
while len(Graphe) > 0:
    # ListeDegre = DegreSommet(Graphe)
    # #print("Liste degré : ", ListeDegre)
    # maxi = degreMax(ListeDegre)
    value = list(Graphe.values())
    print("value = ", value)
    key = list(Graphe.keys())
    maxi = key[value.index(max(value))]
    print("maxi : ", maxi)
    Graphe, ListeEdition, Explore = creerClique(Graphe, maxi, ListeEdition, Explore)
    #print("Graphe après édition des arêtes : ", Graphe)
    #print("Liste Edition : ", ListeEdition)
    Graphe, ListeEdition, Explore = grapheSansClique(Graphe, ListeEdition, Explore)
# print("Graphe : ", Graphe)
#print("ListeEdition ", ListeEdition)
print("Nombre d'éditions ", len(ListeEdition))
#print("Explore : ", Explore)
print("Taille Explore ", len(Explore))
#toc_algo = time.perf_counter()
#print(f"Création d'une union de clique en {toc_algo - tic_algo:0.2f} secondes")
# print(f"Temps total: {toc_algo - debut:0.2f} secondes")


