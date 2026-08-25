def move_zeroes(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        while left < right and arr[left] != 0:
            left += 1

        while left < right and arr[right] == 0:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


arr = [1, 0, 2, 3, 0, 4, 0, 1]
move_zeroes(arr)
print("Array after moving zeroes: ", arr)
