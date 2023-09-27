file = open("./instances/tsp1.txt")

# dans le fichier que l'on utilise on a deux colones chaqu'unes représentant un x et un y
def parseFile (file) :
    content = file.read()
    coord = content.split("/n")
    print(coord[:10])

parseFile(file)