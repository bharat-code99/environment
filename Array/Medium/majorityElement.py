def majority_element(arr):
    elm_count: dict[int, int] = {}
    for num in arr:
        elm_count[num] = elm_count[num] + 1
    

arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]
print("Majority Element: ", majority_element(arr))