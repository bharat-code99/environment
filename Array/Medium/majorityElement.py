def majority_element(arr):
    element = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if count == 0:
            element = arr[i]
        if arr[i] == element:
            count += 1
        elif arr[i] != element:
            count = max(count-1, 0)
    return element

arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]
print("Majority Element: ", majority_element(arr))