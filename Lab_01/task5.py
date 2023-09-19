import numpy as np
salami = np.array([4,5,6,6,4,3,6,4])
dup_elm = np.array([0,0,0,0,0,0,0,0,0,0,0])

def protectSalami(salami):
    loop_count = 0

    for i in range(len(salami)):
        count = 1 

        for j in range(i+1,len(salami)): 
            if salami[i] == salami[j] and salami[i]!=0 :
                count += 1 
                salami[j] = 0

        salami[i] = 0
        
        if count >1:
            dup_elm[loop_count]= count
            loop_count += 1
        
    for i in range(len(dup_elm)):
        if dup_elm[i+1] == 0:
            break

        elif dup_elm[i] == dup_elm[(i+1)]:
            out_put = True

        else:
            out_put = False

    return out_put


print(protectSalami(salami))