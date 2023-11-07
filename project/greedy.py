import time
import util

def glouton (x: list, y: list, isDebug: bool = False, isRandomised: bool = True, start_index: int = 0) :
    chrono_init = time.time()
    dist = 0
    l = len(x)
    util.randomiseFirstItem(isRandomised, x, y)
    if isDebug : loop_time = 0
    for i in range(start_index, l-1):
        if isDebug : loop_time = time.time()
        closest,distToAdd = util.findClosest(i, x, y, True, isDebug)
        util.swap(i+1, closest, x, y, isDebug)
        dist += distToAdd
        if isDebug :
            loop_time = time.time() - loop_time	 
            print (loop_time)
    dist += util.distance(0,l-1, x, y)
    computationTime = time.time() - chrono_init
    if start_index == 0: 
        return(dist, computationTime)
    else :
        return([x,y])