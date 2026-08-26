def linear_search(arr, k):
    idx = -1
    for i in range(len(arr)):
        if arr[i] == k:
            idx = i
            break

    return idx


arr = [1, 2, 3, 4, 5, 6, 7]
print("Element found at index: ", linear_search(arr, 8))