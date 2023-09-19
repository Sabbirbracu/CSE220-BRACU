import numpy as np
cards = np.array([10,2,30,2,50,2,2,0,0])

def discardsCard(x,y):

    i = 0
    while i < len(x):

        if x[i] == y:
            idx = i
            for j in range(len(x)-i-1):

                x[idx] = x[idx+1]
                idx += 1
            x[len(x)-1] = 0

        else:
            i +=1
    return x

    
print(discardsCard(cards,2))












