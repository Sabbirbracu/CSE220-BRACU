# Playing with Array and Probability Theory

def calculate_mean(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    mean = sum / len(arr)
    return mean

def calculate_standard_deviation(arr):
    mean = calculate_mean(arr)
    sum_of_x_minus_x_bar = 0
    for i in range(len(arr)):
        sum_of_x_minus_x_bar += (arr[i] - mean) ** 2
    std_deviation = (sum_of_x_minus_x_bar / (len(arr) - 1)) ** 0.5
    return std_deviation


def arr_of_15(arr):
  mean = calculate_mean(arr)
  std_deviation = calculate_standard_deviation(arr)
  new_arr_length = 0

  for i in range(len(arr)):
    if arr[i] < mean - std_deviation * 1.5 or arr[i] > mean + std_deviation * 1.5:
      new_arr_length += 1

  if new_arr_length == 0:
    return None

  nArr = [0] * new_arr_length

  j = 0
  for i in range(len(arr)):
    if arr[i] < mean - std_deviation * 1.5 or arr[i] > mean + std_deviation * 1.5:
      nArr[j] = arr[i]
      j += 1
  
  return nArr


new_arr = [10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]
print(arr_of_15(new_arr))