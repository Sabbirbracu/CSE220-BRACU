def print_array_recursive(arr, index):
    if index < len(arr):
        print(arr[index])
        print_array_recursive(arr, index + 1)

array = [1, 2, 3, 4, 5]
print("Printing the array recursively:")
print_array_recursive(array, 0)
