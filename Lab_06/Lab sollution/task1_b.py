def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
num = int(input("Enter a positive integer: "))
result = fibonacci(num)
print(f"The {num}-th Fibonacci number is {result}")