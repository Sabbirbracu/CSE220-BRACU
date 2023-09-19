def playRight(sequence,beat):
    
    for i in beat:
        if i ==0:
            pass
        else:
            j = len(sequence)-1
            temp = sequence[j]
            for i in range(len(sequence)):
                if i == len(sequence)-1:
                    sequence[0]=temp
                else:
                    sequence[j] = sequence[j-1]  
                    j = j-1
    print(sequence)

sequence = [10,20,30,40,50,60]
beat = [1,0,0,1,0,1]
        
print(playRight(sequence, beat))