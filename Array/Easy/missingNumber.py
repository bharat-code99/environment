def missing_number(arr):
    n = len(arr) + 1
    expected_sum = (n * (n+1)) // 2
    sum = 0
    for num in arr:
        sum += num

    return expected_sum - sum


arr = [8, 2, 4, 5, 3, 7, 1]
print("Missing Number: ", missing_number(arr))
