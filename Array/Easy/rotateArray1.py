def rotate_array_1(arr):
    first = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]

    arr[-1] = first


arr = [1, 2, 3, 4, 5, 6]
rotate_array_1(arr)
print("Rotated Array: ", arr)