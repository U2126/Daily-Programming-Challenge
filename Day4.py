def merge(arr1, arr2, m, n):
    # Helper function to calculate next gap
    def next_gap(gap):
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)

    gap = m + n
    gap = next_gap(gap)

    while gap > 0:
        # Compare elements in arr1
        i = 0
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        # Compare between arr1 and arr2
        j = gap - m if gap > m else 0
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        # Compare elements in arr2
        if j < n:
            k = 0
            while j + k + gap < n:
                if arr2[j + k] > arr2[j + k + gap]:
                    arr2[j + k], arr2[j + k + gap] = arr2[j + k + gap], arr2[j + k]
                k += 1

        gap = next_gap(gap)

# Example usage:
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merge(arr1, arr2, len(arr1), len(arr2))
print("arr1 =", arr1)
print("arr2 =", arr2)
