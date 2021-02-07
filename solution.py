import fileinput
import time
from collections import defaultdict, Counter
from datetime import datetime

# debut = time.perf_counter()
print("heure début: ", str(datetime.now()))
#On crée une liste vide d'arêtes pour y mettre celles du fichier en entrée:
# Liste_aretes=[]

# for line in fileinput.input():
#     if line[0].isdigit():
#         line=line.split()
#         Liste_aretes.append((int(line[0]),int(line[1])))

Graphe = defaultdict(list)
for line in fileinput.input():
    if line[0].isdigit():
        u,v = (int(x) for x in line.split())
        if not u in Graphe:
            Graphe[u] = []
        if not v in Graphe:
            Graphe[v] = []
        Graphe[u].append(v)
        Graphe[v].append(u)

fileinput.close()

# Liste_aretes=sorted(Liste_aretes)
# print("Taille liste des arêtes: ", len(Liste_aretes))

# lecture_file = time.perf_counter()
# print(f"Lecture du fichier en {lecture_file - debut:0.2f} secondes")

# #On créer un graphe à partir de la liste d'arêtes:
# def CreerGraphe(Liste_aretes):
#     Graphe = defaultdict(list)
#     for u, v in Liste_aretes:
#         Graphe[u].append(v)
#         Graphe[v].append(u)
#     return Graphe


#On veut récupérer le sommet ayant le plus de voisins
#On itère sur chaque voisin pour voir s'il a lui aussi des arêtes avec les autres voisins du sommet initial.
#Si non, on ajoute l'arête manquante. Et on supprime les arêtes qui vont vers d'autres sommets que les voisins du sommet initial.

#Fonction pour supprimer une arête du graphe
#On parcourt les voisins des sommets et on supprimer le sommet correspondant.
#On utilise del plutôt que pop() car plus rapide
def supprimerArete(Graphe, u,v):
    i = 0
    while i < len(Graphe[u]):
        if Graphe[u][i] == v:
            del Graphe[u][i]
        i+=1
    j = 0
    while j < len(Graphe[v]):
        if Graphe[v][j] == u:
            del Graphe[v][j]
        j+=1
    return Graphe


def ajoutArete(Graphe, u, v):
    if v not in Graphe[u]:
        Graphe[u].append(v)
    if u not in Graphe[v]:
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
        Explore.append(v)
        for w in Graphe[u]:#pour un voisin de u, on regarde si w n'est pas déjà un voisin de v, si non, on ajoute l'arête
            if w not in Graphe[v] and w != v:
                Graphe = ajoutArete(Graphe, w, v)
                ListeEdition.append((w,v))
        for w in Graphe[v]:#pour un voisin de v, s'il n'est pas voisin de u, on le supprime de v
            if w not in Graphe[u] and w != u:
                A_Supprimer.append((w,v))
                ListeEdition.append((w,v))
        for w in A_Supprimer:
            Graphe = supprimerArete(Graphe, w[0], w[1])
    return Graphe, ListeEdition, Explore

# Graphe sans les sommets dans Explore
def grapheSansClique(Graphe, ListeEdition, Explore):
    for i in Explore:
        if Graphe[i] not in Explore:
            Graphe.pop(i)
    # print("Nouveau graphe sans clique ", Graphe)
    return Graphe, ListeEdition, Explore

def UnionClique(Graphe):
    ListeEdition = []
    Explore = []
    ListeDegre = {}
    maxi = None
    while len(Graphe) != 0:
        ListeDegre = DegreSommet(Graphe)
        maxi = degreMax(ListeDegre)
        Graphe, ListeEdition, Explore = creerClique(Graphe, maxi, ListeEdition, Explore)
        Graphe, ListeEdition, Explore = grapheSansClique(Graphe, ListeEdition, Explore)
    # print("ListeEdition ", ListeEdition)
    # print("Explore ", Explore)
    return Graphe, ListeEdition, Explore


# Graphe = CreerGraphe(Liste_aretes)
# print("Graphe = ", Graphe)
# tic = time.perf_counter()
# Graphe = CreerGraphe(Liste_aretes)
# Graphe, ListeEdition, Explore = UnionClique(Graphe)
# print("Graphe = ", Graphe)
# toc = time.perf_counter()
# print(f"Création du graphe en {toc - tic:0.2f} secondes")
print("Taille Graphe = ", len(Graphe))
# print(Graphe)
# tic_algo = time.perf_counter()
# ListeEdition = []
# Explore = []
# ListeDegre = {}
# maxi = None
# while len(Graphe) > 0:
#     # ListeDegre = DegreSommet(Graphe)
#     # #print("Liste degré : ", ListeDegre)
#     # maxi = degreMax(ListeDegre)
#     maxi = max(Graphe, key= lambda x: len(set(Graphe[x]))) //2
#     # value = list(len(Graphe.items()[1]))
#     # print("value = ", value)
#     # key = list(Graphe.keys())
#     # maxi = key[value.index(max(value))]
#     # print("maxi : ", maxi)
#     Graphe, ListeEdition, Explore = creerClique(Graphe, maxi, ListeEdition, Explore)
#     #print("Graphe après édition des arêtes : ", Graphe)
#     #print("Liste Edition : ", ListeEdition)
#     Graphe, ListeEdition, Explore = grapheSansClique(Graphe, ListeEdition, Explore)
# print("Graphe : ", Graphe)
#print("ListeEdition ", ListeEdition)
Graphe, ListeEdition, Explore = UnionClique(Graphe)
print("Nombre d'éditions ", len(ListeEdition))
#print("Explore : ", Explore)
print("Taille Explore ", len(Explore))
print("heure fin: ", str(datetime.now()))
#toc_algo = time.perf_counter()
#print(f"Création d'une union de clique en {toc_algo - tic_algo:0.2f} secondes")
# print(f"Temps total: {toc_algo - debut:0.2f} secondes")


