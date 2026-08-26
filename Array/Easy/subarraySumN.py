def subarray_length(arr, k):
    sum_map: dict[int, int] = {}
    curr_sum = 0
    max_len = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == k:
            max_len = i+1
        rem = curr_sum - k
        if rem in sum_map:
            max_len = max(max_len, i-sum_map[rem])
        if curr_sum not in sum_map:
            sum_map[curr_sum] = i
    return max_len


arr = [6, -2, 2, -8, 1, 7, 4, -10]
print("Max subarray length of sum 6: ", subarray_length(arr, 0))