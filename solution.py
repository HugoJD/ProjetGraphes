import fileinput
from collections import defaultdict, Counter

#On crée une liste vide d'arêtes pour y mettre celles du fichier en entrée:
Liste_aretes=[]

for line in fileinput.input():
    if line[0].isdigit():
        line=line.split()
        Liste_aretes.append((int(line[0]),int(line[1])))

fileinput.close()

Liste_aretes=sorted(Liste_aretes)
print("Liste des arêtes: ", Liste_aretes)

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
    print("u = ", u)
    print("v = ", v)
    i = 1
    while i < len(Graphe[u]):
    # for i in range(0,len(Graphe[u])-1):
        print("len de u",len(Graphe[u]))
        print("i = ",i)
        print("Voisins de ", u, ":",Graphe[u])
        print("Voisin comparé de u", Graphe[u][i])
        if Graphe[u][i] == v:
            print("premier if ",Graphe[u][i])
            del Graphe[u][i]
        i+=1
    j = 0
    while j < len(Graphe[v]):
    # for j in range(0,len(Graphe[v])-1):
        print("len de v",len(Graphe[v]))
        print("j = ",j)
        print("Voisins de ", v, ":",Graphe[v])
        print("Voisin comparé de v", Graphe[v][j])
        if Graphe[v][j] == u:
            print("deuxième if ",Graphe[v][j])
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
    for i in range(1,len(Graphe)):
        ListeDegre[i] = len(Graphe[i])
    return ListeDegre

def degreMax(ListeDegre):
     value = list(ListeDegre.values())
     key = list(ListeDegre.keys())
     return key[value.index(max(value))]


def creerClique(Graphe, u):
    ListeEdition = []
    Explore = [u]
    for v in Graphe[u]:
        Explore.append(v)
        for w in Graphe[u]:
            if w not in Graphe[v] and w != v:
                Graphe = ajoutArete(Graphe, w, v)
                ListeEdition.append((w,v))
        for w in Graphe[v]:
            if w not in Graphe[u] and w != u:
                Graphe = supprimerArete(Graphe, w, v)
                ListeEdition.append((w,v))
    print("Explore : ", Explore)
    print("Liste Edition : ", ListeEdition)
    return Graphe

# Recommencer à créer une clique sans les sommets dans Explore


Graphe = CreerGraphe(Liste_aretes)
print("Graphe = ", Graphe)
# Graphe = ajoutArete(Graphe, 2, 5)
# print("Graphe après ajout = ", Graphe)
# Graphe = supprimerArete(Graphe, 5, 4)
# print(Graphe)
#Graphe = supprimerArete(Graphe, 1, 2)
#print("Nouveau Graphe après suppression ", Graphe)
#Graphe = ajoutArete(Graphe, 1,5)
#print("Nouveau Graphe après ajout : ", Graphe)
ListeDegre = DegreSommet(Graphe)
print("Liste degrés = ", ListeDegre)
print("Sommet avec plus grand degré : ", degreMax(ListeDegre))
degreMax = degreMax(ListeDegre)
print("Clique avec voisins de", degreMax," : ", creerClique(Graphe, degreMax))
