import random as rd

# On met en place l'algorythme de test de proche en proche 
#   - on echange deux éléments
#   - on calcule la nouvelle distance
def solve (x: list, y: list) :
    l = len(x)
    ind1 = rd.randint(0,l-1) # on tire aléatoirement deux indices
    ind2 = rd.randint(0,l-1) 