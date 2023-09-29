import greedy 
import random as rd


# Dans ce TP tout est fait sur la mémoire centrale et les listes x et y sont modifiées en place pour un gain d'efficacité !
filePath = "./instances/tsp1.txt"
file = open(filePath)


# Dans le fichier que l'on utilise on a deux colones chaqu'unes représentant un x et un y
def parseFile (file) :
    content = file.read()
    coord = content.split("\n")
    coord.pop(0)
    x = []
    y = []
    for i in range(len(coord)) :
        coord[i] = coord[i].split(" ")
        x.append(int(coord[i][0]))
        y.append(int(coord[i][1]))
    return(x, y)


# Resoltion du problème 
x,y = parseFile(file)
print(greedy.glouton(x,y))