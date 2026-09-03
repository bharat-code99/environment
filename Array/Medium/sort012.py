def sort_012(arr):
    low = mid = count = 0
    high = len(arr) - 1

    while mid <= high:
        count += 1
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    print(f"Loop ran {count} times")
    return arr


arr = [2, 0, 2, 1, 1, 0]
print("Sorted Array: ", sort_012(arr))