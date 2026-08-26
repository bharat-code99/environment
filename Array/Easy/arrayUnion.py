def merge_array(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    res = []

    i = j = 0
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    res.extend(arr1[i:])
    res.extend(arr2[j:])

    return res


nums1 = [1, 3, 5, 7, 9]
nums2 = [2, 4, 6, 8]

union = merge_array(nums1, nums2)

print("Merged Array: ", union)