import numpy as np

def landscape(m):
    row,col = m.shape
    print(row,col)

    new_arr = np.zeros((col,row),dtype=int)  # for creating multidimentional arrayt with 0 

    for i in range(col):

        for j in range(row):
            new_arr[i][j] = m[j][i]
    print(new_arr)


m = np.array([[7,11,8],[6,9,14],[0,4,7],[2,0,8]])
landscape(m)