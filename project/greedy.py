import time
import util

def glouton (x: list, y: list) :
    chrono_init = time.time()
    dist = 0
    l = len(x)
    util.randomiseFirstItem(True, x, y)
    for i in range(l-1):
        closest,distToAdd = util.findClosest(i, x, y, True)
        util.swap(i+1, closest, x, y)
        dist += distToAdd
    dist += util.distance(0,l-1, x, y)
    computationTime = time.time() - chrono_init
    return(dist, computationTime)