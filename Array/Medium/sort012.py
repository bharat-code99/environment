def sort_012(arr):
    left, right = 0, len(arr) - 1
    i = 0
    while i <= right:
        if arr[i] == 0:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        elif arr[i] == 2:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
        elif arr[i] == 1:
            i += 1
    return arr


arr = [2, 0, 2, 1, 1, 0]
print("Sorted Array: ", sort_012(arr))