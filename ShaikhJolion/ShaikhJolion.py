import fileinput
from collections import defaultdict
import signal
import time

class Killer:
  exit_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit)
    signal.signal(signal.SIGTERM, self.exit)

  def exit(self,signum, frame):
    self.exit_now = True

killer = Killer()

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
    for v in Graphe[u]:#on regarde chaque voisin de u
        Explore.append(v)
        for w in Graphe[u]:#pour un voisin de u, on regarde si w n'est pas déjà un voisin de v, si non, on ajoute l'arête
            if w not in Graphe[v] and w != v:
                ListeEdition.append((w,v))
                Graphe = ajoutArete(Graphe, w, v)
        i=0
        while i < len(Graphe[v]):
            if Graphe[v][i] not in Graphe[u] and Graphe[v][i] != u:
                ListeEdition.append((v,Graphe[v][i]))
                Graphe = supprimerArete(Graphe, Graphe[v][i], v)
            else:
                i+=1
    return Graphe, ListeEdition, Explore


# Graphe sans les sommets dans Explore
def grapheSansClique(Graphe, ListeEdition, Explore):
    for i in Explore:
        if Graphe[i] not in Explore:
            Graphe.pop(i)
    return Graphe, ListeEdition, Explore

def UnionClique(Graphe):
    ListeEdition = []
    Explore = []
    ListeDegre = {}
    maxi = None
    while len(Graphe) != 0:
        if killer.exit_now:
            break
        ListeDegre = DegreSommet(Graphe)
        maxi = degreMax(ListeDegre)
        Graphe, ListeEdition, Explore = creerClique(Graphe, maxi, ListeEdition, Explore)
        Graphe, ListeEdition, Explore = grapheSansClique(Graphe, ListeEdition, Explore)
    return Graphe, ListeEdition, Explore

#Début du programme

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

ListeEdition = []
Explore = []
Graphe, ListeEdition, Explore = UnionClique(Graphe)
#Affichage des arêtes éditées:
for i in ListeEdition:
    print(i[0], i[1])

#fin du programme



