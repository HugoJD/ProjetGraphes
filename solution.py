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
    for i in range(0,len(Graphe[u])-1):
        if Graphe[u][i] == v:
            del Graphe[u][i]
    for j in range(0,len(Graphe[v])-1):
        if Graphe[v][j] == u:
            del Graphe[v][j]
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
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     value = list(ListeDegre.values())
     key = list(ListeDegre.keys())
     return key[value.index(max(value))]

#Parcourir chaque voisin du sommet de départ puis ajouter les arêtes manquantes entre ses voisins. 
def creerClique(Graphe, u):
    clique = [u]
    for v in Graphe[u]:
        clique.append(v)
        #pour chaque voisin de u, on ajoute les arêtes entre ses voisins
        for w in Graphe[v]:
            if w not in Graphe[u] and w != v: 
                print("Voisin de ", u, " : ", w)
                Graphe = ajoutArete(Graphe, w, v)
                print("arête ajoutée: ", w, v)
            if w in Graphe[u] and w != v:
                print("pas voisin de ", u, " mais de : ", v, " : ", w)
                Graphe = supprimerArete(Graphe, w, v)
                print("arête supprimée: ", w, v)
    print(clique)   
    return Graphe



Graphe = CreerGraphe(Liste_aretes)
print("Graphe = ", Graphe)
#Graphe = supprimerArete(Graphe, 1, 2)
#print("Nouveau Graphe après suppression ", Graphe)
#Graphe = ajoutArete(Graphe, 1,5)
#print("Nouveau Graphe après ajout : ", Graphe)
ListeDegre = DegreSommet(Graphe)
print("Liste degrés = ", ListeDegre)
print("Sommet avec plus grand degré : ", degreMax(ListeDegre))
print("Clique avec voisins de 5: ", creerClique(Graphe, 5))
