def trap(height):
    n = len(height)
    if n < 3:  # Less than 3 bars -> no water can be trapped
        return 0

    left, right = 0, n - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


# 🔹 Test Cases
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Output: 6
print(trap([4, 2, 0, 3, 2, 5]))                    # Output: 9
print(trap([1, 1, 1]))                             # Output: 0
print(trap([5]))                                   # Output: 0
print(trap([2, 0, 2]))                             # Output: 2
