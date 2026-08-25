def get_second_largest(arr):
    if len(arr) < 2:
        return -1

    largest = -1
    s_largest = -1

    for i in range(len(arr)):
        if arr[i] > largest:
            s_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > s_largest:
            s_largest = arr[i]

    return s_largest


arr = [7,7,7,7,7,7,7]
print("Second Largest Element: ", get_second_largest(arr))