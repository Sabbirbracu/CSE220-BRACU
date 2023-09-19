def print_pattern(n, current=1, spaces=0):
    if current > n:
        return
    else:
        for i in range(n - current):
            print(" ", end=" ")
        for i in range(1, current + 1):
            print(i, end=" ")
        print()
        print_pattern(n, current + 1)

# Test the function
num = int(input("Enter a number: "))
print_pattern(num)
