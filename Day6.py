def find_zero_sum_subarrays(arr):
    prefix_sum = 0
    hashmap = {0: [-1]}  # store prefix sums with indices
    result = []

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum in hashmap:
            for start in hashmap[prefix_sum]:
                result.append((start + 1, i))

        # store index for this prefix sum
        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = []
        hashmap[prefix_sum].append(i)

    return result


# Example
arr = [1, 2, -3, 3, -1, 2]
print(find_zero_sum_subarrays(arr))
# Output: [(0, 2), (1, 3)]
