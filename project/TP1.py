# L'obectif de ce TP est d'implémenter le chemin hamiltonien contenue dans ces fichiers avec plusieurs agorithmes
import math
import time
import random as rd


# Dans ce TP tout est fait sur la mémoire centrale et les listes x et y sont modifiées en place pour un gain d'efficacité !
filePath = "./instances/tsp1.txt"
file = open(filePath)


# Dans le fichier que l'on utilise on a deux colones chaqu'unes représentant un x et un y
def parseFile (file) :
    content = file.read()
    coord = content.split("\n")
    l = int(coord.pop(0))
    x = []
    y = []
    for i in range(len(coord)) :
        coord[i] = coord[i].split(" ")
        x.append(int(coord[i][0]))
        y.append(int(coord[i][1]))
    return(x, y, l)

def randomiseFirstItem (cond : bool) :
    if cond :
        seed = rd.randint(0, l-1)
        swap(0, seed)


# On fait nos fonction auxiliaire
def distance(ind1 : int, ind2 : int) :
    return (math.sqrt((x[ind1]-x[ind2])**2 + (y[ind1]-y[ind2])**2))

def findClosest (ind : int, iter = False):
    res =  0 if ind != 0 else 1
    min_dist = distance(ind, res)
    end = l if iter else l-i # permet de traiter avec une meme fonction la recherche en place avec l'algo glouton est une recherche
    start = 0 if iter else i # dans toute la liste du plus près
    for i in range(start, end):
        if i != ind : 
            dist = distance(ind, i)
            if dist < min_dist :
                min_dist = dist
                res = i
    return (res, min_dist)

def swap(ind1 : int, ind2 : int) :
    x[ind1],x[ind2] = x[ind2],x[ind1]
    y[ind1],y[ind2] = y[ind2],y[ind1]


# On initie notre recherche avec un algo glouton
def glouton () :
    chrono_init = time.time()
    dist = 0
    randomiseFirstItem(False)
    for i in range(l-1):
        closest,distToAdd = findClosest(i, True)
        swap(i+1, closest)
        dist += distToAdd
    dist += distance(0,l-1)
    computationTime = time.time() - chrono_init
    return(dist, computationTime)


# On met en place l'algorythme de test de proche en proche 
#   - on echange deux éléments
#   - on calcule la nouvelle distance
def solve (configuation) :

    print ("issou")


# parametres de test 
naiveTestListe = [[1, 2, 15, 6], [10, 3, 7, 1]]

# Resoltion du problème 
x,y,l = parseFile(file)
print(glouton())
