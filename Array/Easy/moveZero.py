def move_zeroes(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1

    while i < len(arr):
        arr[i] = 0
        i += 1


# [1, 2, 3, 4, 1, 0, 0, 0]
arr = [1, 0, 2, 3, 0, 4, 0, 1]
move_zeroes(arr)
print("Array after moving zeroes: ", arr)
