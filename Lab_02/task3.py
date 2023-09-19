import numpy as np

def verify_seating_arrangement(seats, number):
    row,col= seats.shape
    for i in range(row):
        for j in range(row):
            if i != j:
                diff = (seats[i][j] - seats[j][i])
                if diff != number:
                    return False
    return True

seats = np.array([
    [8, 15, 7, 12],
    [13, 2, 18, 11],
    [9, 20, 5, 2],
    [14, 9, 0, 10]])

#seats = np.array([[7,13,9,14],[12,8,15,11],[10,17,3,2],[15,10,1,4]])
number = 1

result = verify_seating_arrangement(seats, number)
print(result)
