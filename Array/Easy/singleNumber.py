def get_single(arr):
    xorr = 0

    for num in arr:
        xorr ^= num

    return xorr


arr = [4, 1, 2, 1, 2]
print("Single Number: ", get_single(arr))