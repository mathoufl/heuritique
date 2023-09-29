import math
import time
import random as rd

def swap(ind1: int, ind2: int, x: list, y: list) :
    x[ind1],x[ind2] = x[ind2],x[ind1]
    y[ind1],y[ind2] = y[ind2],y[ind1]


def randomiseFirstItem (cond : bool, x: list, y: list) :
    l = len(x)
    if cond :
        seed = rd.randint(0, l-1)
        swap(0, seed, x, y)

def distance(ind1 : int, ind2 : int, x: list, y: list) :
    return (math.sqrt((x[ind1]-x[ind2])**2 + (y[ind1]-y[ind2])**2))

def findClosest (ind : int, x: list, y: list, iter = False):
    res =  0 if ind != 0 else 1
    l = len(x)
    min_dist = distance(ind, res, x, y)
    end = l if iter else l-i # permet de traiter avec une meme fonction la recherche en place avec l'algo glouton est une recherche
    start = 0 if iter else i # dans toute la liste du plus près
    for i in range(start, end):
        if i != ind : 
            dist = distance(ind, i, x, y)
            if dist < min_dist :
                min_dist = dist
                res = i
    return (res, min_dist)