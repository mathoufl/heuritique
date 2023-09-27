import math
import matplotlib
import random as rd

coord = [[288, 273], [54, 228], [78, 276], [297, 147], [99, 189], [189, 210], [195, 252], [210, 279], [237, 87], [114, 228], [388, 373], [154, 328], [178, 376], [397, 247], [199, 289], [289, 310], [295, 352], [310, 379], [337, 187], [214, 328]]

    
def distance(point1, point2) :
    return (math.sqrt((coord[point1][0]-coord[point2][0])**2 + (coord[point1][1]-coord[point2][1])**2))

def closest (point, list):
    min = distance(point, list[0])
    res = list[0]
    for i in list:
        dist = distance(point, i)
        if dist < min :
            min = dist
            res = i
    return (res, min)

def parcours () :
    visites = [0]
    restants = [i+1 for i in range(len(coord)-1)]
    dist_tot = 0
    while len(restants) >= 1 :
      point,dist = closest(visites[-1], restants)
      visites.append(point)
      restants.remove(point)
      dist_tot += dist
    dist_tot += distance(0, visites[-1])
    return (visites, dist_tot)

print(parcours())