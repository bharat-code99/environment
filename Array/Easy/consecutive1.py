def consecutive_one(arr):
    current = 0
    most = 0

    for num in arr:
        if num == 1:
            current += 1
            most = max(most, current)
        else:
            current = 0

    return most


arr = [1, 0, 1, 1, 0, 1]
print("Most consecutive Ones:", consecutive_one(arr))