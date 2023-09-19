import numpy as np

def walk_zigzag(floor):

    row,col = floor.shape
    
    for i in range(row):
        x = ""
        y = ""
        if i % 2 == 0 or i ==0 :
            for j in range(0,col,2):
                x += f"{floor[i][j]} "
            print(x)

        elif i % 2 != 0:
            for j in range(col-1,0,-2):
                 y += f"{floor[i][j]} "
            print(y)

floor = np.array([[ '3W' , '8B' , '4W' , '6B' , '1W' , '5B'],
                  ['3B' , '2W' , '1B' , '6W' , '3B' , '8W'],['9W' , '0B' , '7W' , '5B' , '3W' , '8B'],
                  ['2B' , '1W' , '3B' , '6W' , '0B' , '4W'],['1W' , '4B' , '2W' , '8B' , '6W' , '6B']])
walk_zigzag(floor)