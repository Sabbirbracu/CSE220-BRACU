def balanceSalami(salami):
    total_sum = sum(salami)
    left_sum = 0
    right_sum = total_sum

    for i in range(len(salami) - 1):
        left_sum += salami[i]
        right_sum -= salami[i]
        if left_sum == right_sum:
            return True

    return False

# Test cases
salami = [10, 3, 1, 2, 10]
print(balanceSalami(salami))  # Output: True
