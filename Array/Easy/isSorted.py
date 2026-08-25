def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False

    return True


arr = [1, 2, 3, 6, 5]
print("Is array sorted: ", is_sorted(arr))