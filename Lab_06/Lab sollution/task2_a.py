def decimal_to_binary(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return decimal_to_binary(n // 2) + str(n % 2)


decimal_num = int(input("Enter a decimal number: "))
binary_result = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is {binary_result}")
