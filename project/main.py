import greedy 
import util
import genetic

# Dans ce TP tout est fait sur la mémoire centrale et les listes x et y sont modifiées en place pour un gain d'efficacité !
filePath = "./instances/tsp1.txt"
file = open(filePath)

# Initialisation des variables
isDebug = False
genetic_population_size = 10
genetic_max_itérations = 100
genetic_invariant = 5
genetic_survivor_number = 4
genetic_max_point_selector = 250

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


x,y = parseFile(file)
x_test, y_test = [1,10,8,11,5,18,16],[22,6,14,7,4,1,10]

## Running greedy
print(greedy.glouton(x, y, isDebug)) # résultat sans seed: 29444 en 0.9s

## Runing genetic algorythme
print(genetic.genetic(x, y, genetic_population_size, genetic_max_itérations, genetic_invariant, genetic_survivor_number, genetic_max_point_selector, isDebug)) # résultat :  

print ("done")