def get_largest(arr: list[int]) -> int:
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest


arr = [2, 5, 1, 3, 10]
print("Largest Element: ", get_largest(arr))