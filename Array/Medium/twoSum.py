def two_sum(arr, k):
    num_with_idx = sorted([(num, idx) for idx, num in enumerate(arr)], key=lambda x: x[0])

    left, right = 0, len(arr)-1

    while left < right:
        curr_sum = num_with_idx[left][0] + num_with_idx[right][0]

        if curr_sum == k:
            return [num_with_idx[left][1], num_with_idx[right][1]]
        elif curr_sum < k:
            left += 1
        else:
            right -= 1

    return [-1, -1]


arr = [2, 6, 5, 8, 11]

print(f"Indices of the sum {16}", two_sum(arr, 16))