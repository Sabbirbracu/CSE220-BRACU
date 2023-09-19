import numpy as np

pokemon_1 = np.array([4, 5, -1, None, None])
pokemon_2 = np.array([2, 27, 7, 12, None])

def mergeLineup(x,y):
    new_pokemon = np.array([0,0,0,0,0])
    j = len(x)-1
    for i in range(len(x)):
        
        if x[i]== None:
            x[i] = 0
        elif y[j] == None:
            y[j] = 0

        new_pokemon[i] = x[i] + y[j]
        j -= 1
    return new_pokemon


print(mergeLineup(pokemon_1,pokemon_2))


