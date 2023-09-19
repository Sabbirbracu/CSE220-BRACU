import numpy as np

arr = np.array([45,23,78,84,41])
new_arr = np.zeros(len(arr),dtype=int)
print(new_arr)

def waveYourFlag(x):

    new_arr[0] = arr[0]


    if arr[0] % 2 == 0:    
        # i am checking the next element
        for i in range(1,len(arr)):
            if i % 2 != 0:
                if arr[i] % 2 == 0:
                    j = i+1
                    while j < len(arr):
                        if arr[j] % 2 != 0:
                            new_arr[i] = arr[j]  # using this loop until i found the odd number
                            break
                        else:
                            j +=1
                else:
                    new_arr[i] = arr[i]

            else:
                if arr[i] % 2 != 0:
                    if arr[i-1] % 2 == 0:
                        new_arr[i] = arr[i-1]
                    elif arr[i] % 2 == 0:
                        new_arr[i] = arr[i]
                    else:
                        j = i+1
                        while j < len(arr):
                            if arr[j] % 2 == 0:
                                new_arr[i] = arr[j]
                                break
                            else:
                                j += 1

                else:
                    new_arr[i] = arr[i]

    else:                     # writing this part if the first element is odd number
        for i in range(1,len(arr)):
            if i % 2 != 0:
                if arr[i] % 2 != 0:
                    j = i+1
                    while j < len(arr):
                        if arr[j] % 2 == 0:
                            new_arr[i] = arr[j]
                            break
                        else:
                            j +=1
                else:
                    new_arr[i] = arr[i]

            else:
                if arr[i] % 2 == 0:
                    if arr[i-1] % 2 != 0:
                        new_arr[i] = arr[i-1]
                    elif arr[i] % 2 != 0:
                        new_arr[i] = arr[i]
                    else:
                        j = i+1
                        while j < len(arr):
                            if arr[j] % 2 != 0:
                                new_arr[i] = arr[j]
                                break
                            else:
                                j += 1

                else:
                    new_arr[i] = arr[i]
        

    return new_arr





print(waveYourFlag(arr))



    
