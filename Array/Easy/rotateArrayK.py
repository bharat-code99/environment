def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_array(arr, k, direction):
    n = len(arr)

    if n == 0 or k == 0:
        return arr

    k = k % n

    if direction == "right":
        reverse(arr, 0, n-1)
        reverse(arr, 0, k-1)
        reverse(arr, k, n-1)

    elif direction == "left":
        reverse(arr, 0, k-1)
        reverse(arr, k, n-1)
        reverse(arr, 0, n-1)


arr = [1, 2, 3, 4, 5, 6, 7]
rotate_array(arr, 3, "left")
print("Rotated Array: ", arr)