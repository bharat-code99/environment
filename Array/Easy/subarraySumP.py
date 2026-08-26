def subarray_length(arr, k):
    left = right = 0
    maxLen = -1
    currSum = 0

    while right < len(arr):
        currSum += arr[right]
        if currSum == k:
            maxLen = max(maxLen, right-left+1)
        while currSum > k and left <= right:
            currSum -= arr[left]
            left += 1
        right += 1

    return maxLen


arr = [1, 2, 3, 1, 1, 1, 1, 3, 3]
print("Max subarray length of sum 6: ", subarray_length(arr, 6))