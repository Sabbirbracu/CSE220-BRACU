def powerN(base, n):
    if n == 0:
        return 1
    else:
        return base * powerN(base, n - 1)


print(powerN(3, 1))  
print(powerN(3, 2))  
print(powerN(3, 3)) 