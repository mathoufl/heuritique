import math
import random as rd

def swap(ind1: int, ind2: int, x: list, y: list, isDebug: bool = False) :
    if isDebug : 
        print("configuration before swap :")   
        print ("  x = " + str(x))
        print ("  y = " + str(y))
    x[ind1],x[ind2] = x[ind2],x[ind1]
    y[ind1],y[ind2] = y[ind2],y[ind1]
    if isDebug : 
        print("configuration after swap :")
        print ("  x = " + str(x))
        print ("  y = " + str(y))


def randomiseFirstItem (cond : bool, x: list, y: list) :
    l = len(x)
    if cond :
        seed = rd.randint(0, l-1)
        swap(0, seed, x, y)

def distance(ind1 : int, ind2 : int, x: list, y: list) :
    return (math.sqrt((x[ind1]-x[ind2])**2 + (y[ind1]-y[ind2])**2))

def findClosest (ind : int, x: list, y: list, isgreedy: bool = False, isDebug: bool = False):
    res =  0 if ind != 0 else 1
    res = res if not isgreedy else ind+1
    l = len(x)
    min_dist = distance(ind, res, x, y) # problème d'initialisatin dans min_dist 
    start = 0 if not isgreedy else ind # dans toute la liste du plus près
    for i in range(start, l):
        if i != ind : 
            dist = distance(ind, i, x, y)
            if isDebug : print("distance entre : " + str(ind) + " et " + str(i) + " est de : " + str(dist) + " la valeur de l est de : " + str(l))
            if dist < min_dist :
                min_dist = dist
                res = i
    if isDebug : print("min_dist : " + str(min_dist) + " and the is closest is : " + str(res))
    return (res, min_dist)

def calc_distance_tot(x,y):
    dist = distance(0, len(x)-1, x, y)
    for i in range(len(x)-1):
        dist += distance(i, i+1, x, y)
    return dist