import random
from copy import copy
import sys
from operator import itemgetter, attrgetter
from collections import defaultdict
import fileinput
from datetime import datetime

# heure_debut = datetime.now()
# print("heure début: ", str(heure_debut))

Arretes=[]
Graph=defaultdict(list)

for line in fileinput.input():
    if line[0].isdigit():
        line=line.split()
        Graph[int(line[0])].append(int(line[1]))
        Graph[int(line[1])].append(int(line[0])) 
        

fileinput.close()


def CreerGraphe(Arretes):
    Graph=defaultdict(list)
    for node1, node2 in Arretes:
        Graph[node1].append(node2)
        Graph[node2].append(node1)
    return Graph



# def SupprimerArreteGraph(Graph,Name_node_1,Name_node_2):
#     for i in range(0,len(Graph[Name_node_1])):
#         if Graph[Name_node_1][i]==Name_node_2:
#             del Graph[Name_node_1][i]
#             break
#     for y in range(0,len(Graph[Name_node_2])):
#         if Graph[Name_node_2][y]==Name_node_1:
#             del Graph[Name_node_2][y]
#             break
#     return Graph


# def ExisteArreteGraph(Graph,node1,node2):
#     for i in range(0,len(Graph[node1])-1):
#         if Graph[node1][i]==node2:
#             return True
#     #Il serait anormal d'avoir une arrete enregistree seulement pour un sommet.
#     for y in range(0,len(Graph[node2])-1):
#         if Graph[node2][y]==node1:
#             sys.stderr.write("Il se peut qu'il y ait une erreur dans les donnees")
#             return True
#     return False

# def AjouterArreteGraph(Graph,Name_node_1,Name_node_2):
#     if not ExisteArreteGraph(Graph,Name_node_1,Name_node_2):
#         Graph[Name_node_1].append(Name_node_2)
#         Graph[Name_node_2].append(Name_node_1)
#     return Graph

# def ListerArreteSupprimee(List,node1,node2):
#     List.append((node1,node2))
#     return List

# def ListerArreteAjoutee(List,node1,node2):
#     List.append((node1,node2))
#     return List




# def GetDegreNode(Graph,node):
#     return len(Graph[node])


# def GetVoisins(Graph,node):
#     return Graph[node]


# #Renvoie un sous-graph complet à partir d'un sommet pris dans le Graph
# def GetClique(Graph):
#     ListeClique=set()
#     ListeClique.add(node)
#     Voisins=set(Graph[node])
#     for v in Voisins:
#         VoisinsDuVoisin=set(Graph[v])
#         if (len(VoisinsDuVoisin & Voisins))>0 and (len(ListeClique - VoisinsDuVoisin))==0:
#             ListeClique.add(v)
#     if len(ListeClique)<2:
#         Voisins=list(Voisins)
#         if len(Voisins)>1:
#             ListeClique.add(Voisins[random.randint(0,len(Voisins)-1)])
#         elif len(Voisins)==1:
#             ListeClique.add(Voisins[0])
#     return list(ListeClique)


# def EstUneClique(Graphe,node):
#     voisins=set(Graph[node])
#     nbrVoisin=float(len(voisins))
#     for v in voisins:
#         voisins_2nd=set(Graph[int(v)])
#         degSommet=float(len(voisins & voisins_2nd)+1)
#         if degSommet/nbrVoisin<1:
#             sys.stderr.write("Ce n'est pas une clique : " + str(node) + "\n")
#             return False
#     return True


# def ClasserParDegree(Graph):
#     Classement=[]
#     for v in Graph:
#         Classement.append((v,GetDegreNode(Graph,v)))
#     return sorted(Classement,key=itemgetter(1), reverse=True)

# def VoisinCliqueFortementConnecte(Graph,cliq,critere):
#     ListeArrete=[]
#     Liste=[]
#     Clique=set(cliq)
#     for v in Clique:
#         VoisinClique=set(Graph[v])
#         for w in (VoisinClique - Clique):
#             if len(Clique - set(Graph[w]))<=critere and not(w in Liste):
#                 Liste.append(w)
#                 nonAdj_node_cliq=list(Clique - set(Graph[w]))
#                 for i in nonAdj_node_cliq:
#                     ListeArrete.append((w,i))
#                 return ListeArrete


# #Permet de classer les sommets par degré, prochaine amélioration
# # GraphByDegree=ClasserParDegree(Graph)


# #Ajoute les arrêtes pour connecter les sommets fortements
# #connectés à un sous-graphe complet donné
# # for s in Graph:
# #     Alea=random.randint(0,10)
# #     if Alea<5: 
# #         Clique=GetClique(Graph,s)
# #         AjoutArrete=VoisinCliqueFortementConnecte(Graph, Clique, 3)
# #         if (AjoutArrete is not None) and (len(AjoutArrete)>0) and (len(AjoutArrete)<len(Clique)):
# #             for ajout in AjoutArrete:
# #                 Graph=AjouterArreteGraph(Graph,ajout[0],ajout[1])
# #                 print(str(ajout[0]) + " " + str(ajout[1]))



# #Algo de suppression des arrêtes en trop, pour former des cliques
# for s in Graph:
#     Clique=GetClique(Graph,s)
#     # ArreteAdd=VoisinCliqueFortementConnecte(Graph,Clique,1)
#     # if (ArreteAdd is not None) and (len(ArreteAdd)>0):
#     #     for ajout in ArreteAdd:#Definir le critère en fonction de la taille de la clique
#     #         Graph=AjouterArreteGraph(Graph,ajout[0],ajout[1])
#     #         print(str(ajout[0]) + " " + str(ajout[1]))
#     #     Clique=GetClique(Graph,s)
#     for v in Clique:
#         if len(Clique)-1<GetDegreNode(Graph,v):
#             ListeASupprimer=set()
#             ListeASupprimer=set(Graph[v])-set(Clique)
#             ListeASupprimer=list(ListeASupprimer)
#             for w in ListeASupprimer:
#                 Graph=SupprimerArreteGraph(Graph,v,w)
#                 # print(str(v) + " " + str(w))
        


# #Vérification si les sommets forment bien des cliques
# for v in Graph:
#     EstUneClique(Graph,v)

# heure_fin = datetime.now()
# print("heure fin: ", str(heure_fin))
# print("Temps total algo: ", str(heure_fin - heure_debut))

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



def creerClique(Graphe, ListeEdition, Explore): 
    for u in list(Graphe):#on regarde chaque sommet du graphe
        print("Test")
        Explore.append(u)
        print(u)
        for v in Graphe[u]:
            for w in Graphe[u]:#pour un voisin de v, on regarde si w n'est pas déjà un voisin de u, sinon, on ajoute l'arête
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

ListeEdition = []
Explore = []
print("taille graphe ", Graphe)
print(Graphe)
Graphe, ListeEdition, Explore = creerClique(Graphe, ListeEdition, Explore)
print("taille Explore", len(Explore))