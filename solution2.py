import fileinput
import time
from collections import defaultdict
from datetime import datetime
from random import randint

# debut = time.perf_counter()
heure_debut = datetime.now()
print("heure début: ", str(heure_debut))
#On crée une liste vide d'arêtes pour y mettre celles du fichier en entrée:
Liste_aretes=[]

for line in fileinput.input():
    if line[0].isdigit():
        line=line.split()
        Liste_aretes.append((int(line[0]),int(line[1])))

fileinput.close()

Liste_aretes=sorted(Liste_aretes)
print("Taille liste des arêtes: ", len(Liste_aretes))


# On créer un graphe à partir de la liste d'arêtes:
def CreerGraphe(Liste_aretes):
    Graphe = defaultdict(list)
    for u, v in Liste_aretes:
        Graphe[u].append(v)
        Graphe[v].append(u)
    return Graphe

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


# def ajoutArete(Graphe, u, v):
#     if v not in Graphe[u]:
#         Graphe[u].append(v)
#     if u not in Graphe[v]:
#         Graphe[v].append(u)
#     return Graphe

# on cherche un sous-graphe complet à partir d'un sommet au hasard du graphe
def sousGraphe(Graphe, u):
    Voisins_U = set(Graphe[u]) #On crée un ensemble avec les voisins de u
    sous_graphe = set()
    sous_graphe.add(u) #on cherche le sous-graphe complet contenant u
    for v in Voisins_U: #pour chaque voisin v de u, si u et v on des voisins en commun et si 
        Voisins_v = set(Graphe[v])
        if ((len(Voisins_U & Voisins_v) > 1) and (len(sous_graphe - Voisins_v) == 0)):
            sous_graphe.add(v)
    return list(sous_graphe)

#Depuis le sous-graphe complet, on supprime les arêtes qui relie ce sous-graphe à des sommets externes:
def creerClique(Graphe, sous_graphe, v):
    A_supprimer = set(set(Graphe[v]) - set(sous_graphe))
    for w in list(A_supprimer):
        Graphe = supprimerArete(Graphe,w,v)

Edition = []
Graphe = CreerGraphe(Liste_aretes)
print("Taille Graphe : ", len(Graphe))
for u in Graphe:
    sous_graphe = sousGraphe(Graphe, u)
    for v in sous_graphe:
        if len(sous_graphe)-1 < len(Graphe[v]):
            A_supprimer = set(set(Graphe[v]) - set(sous_graphe))
            for w in list(A_supprimer):
                Graphe = supprimerArete(Graphe,w, v)
                Edition.append((v,w))


print("Nombre d'éditions ", len(Edition))
heure_fin = datetime.now()
print("heure fin: ", str(heure_fin))
print("Temps total algo: ", str(heure_fin - heure_debut))
    








"""
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
"""