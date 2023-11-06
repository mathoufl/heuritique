import time
import random as rd
import util
import greedy

# Mise en place de l'algo genetic 
def genetic (x: list, y: list, population_size: int, max_itérations: int, stable_iteration: int, survivor_number: int, chromosome_max_size: int, isDebug: bool = False) :
    chrono  = time.time()
    # on génére plusieurs individues de la population (ici ce sera plusieurs configurations generées par des greedys avec des seed différents)
    population = init_population(x, y, population_size-1, isDebug) # prend 23 secondes&
    chrono_mid = time.time() - chrono
    print(chrono_mid)
    population_best = []
    while len(population_best) < max_itérations and isBestStable(population_best, stable_iteration) :
        survivors = select_bests(population, survivor_number)
        new_population = breed(survivors, population_size, chromosome_max_size)
        # new_population = mutate(new_population)
        population = generation_clash(population, new_population)
        population_best.append(select_best(population))
    chrono = time.time() - chrono
    return(population_best, chrono)

def init_population(x: list, y: list, population_size: int, isDebug: bool = False):
    population = [[x,y, util.calc_distance_tot(x,y)]]
    for i in range(population_size) :
        x_i = x[:]
        y_i = y[:]
        greedy.glouton(x_i, y_i, isDebug, True)
        population.append([x_i, y_i, util.calc_distance_tot(x_i, y_i)])
    return(population)

def isBestStable(population_best: list, stable_iteration: int) :
    if len(population_best) < stable_iteration : return True
    sample = population_best[-1*stable_iteration : ]
    elem = sample[0]
    return all(i == elem for i in sample)

def select_bests(population: list, survivor_number: int) :
    bests = [[i, population[i][2]] for i in range(survivor_number)]
    for i in range(survivor_number, len(population)-1):
        if(population[i][2] < max([bests[b][1] for b in range(survivor_number)])) :
            bests.append([i, population[i][2]])
            elem_max_bests = max(bests, key=lambda x: x[1])
            bests.remove(elem_max_bests)
    return [population[bests[b][0]] for b in range(len(bests))]

def select_best(population) :
    return max(population, key=lambda x: x[2])

def breed(population, objectif, chromosome_max_size) :
    children_number = objectif - len(population)
    childrens = []
    for i in range(children_number) :
        father = population[rd.randint(0, len(population)-1)]
        mother = population[rd.randint(0, len(population)-1)]
        child = mating(father, mother, chromosome_max_size)
        childrens.append(child)
    return population+childrens

def mating(father, mother, chromosome_max_size) :
    isNot_possible_chromosom_set = True
    while isNot_possible_chromosom_set :
        cfi = rd.randint(0,len(father[0])-chromosome_max_size)
        cfs = rd.randint(0,chromosome_max_size)
        chromosome_father = [father[0][cfi:cfi+cfs],father[1][cfi:cfi+cfs]]
        cmi = rd.randint(0,len(mother[0])-chromosome_max_size)
        cms = rd.randint(0,chromosome_max_size)
        chromosome_mother = [mother[0][cmi:cmi+cms],father[1][cmi:cmi+cms]]
        isNot_possible_chromosom_set = adn_test(chromosome_father, chromosome_mother)
    child = [[chromosome_father[0][i], chromosome_father[1][i]] for i in range(len(chromosome_father[0]))] + [[chromosome_mother[0][i], chromosome_mother[1][i]] for i in range(len(chromosome_mother[0]))]
    formated_father = [[father[0][i], father[1][i]] for i in range(len(father[0]))]
    child += [elem for elem in formated_father if elem not in child]
    child = [[c[0] for c in child],[c[1] for c in child]]
    child = greedy.glouton(child[0], child[1], False, False, cms+cfs)
    child.append(util.calc_distance_tot(child[0], child[1]))
    return(child)

def adn_test(chromosome_father, chromosome_mother) :
    isNotCompatible = False
    for i in range(len(chromosome_father)-1):
        for j in range(len(chromosome_mother)-1):
            if chromosome_father[0][i] == chromosome_mother[0][j] and chromosome_father[1][i] == chromosome_mother[1][j]:
                isNotCompatible = True
    return(isNotCompatible)


def mutate(population) :
    print("mutate")

def generation_clash(old_population, new_population):
    if select_best(old_population)[2] > select_best(new_population)[2] :
        return old_population
    else :
        return new_population