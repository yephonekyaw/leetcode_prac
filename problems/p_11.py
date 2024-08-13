def maxArea(height):
    l, r = 0, len(height) - 1
    max_area = -float('inf')
    while l < r:
        if (max_area < min(height[l], height[r]) * (r - l)):
            max_area = min(height[l], height[r]) * (r - l)

        if (height[l] <= height[r]):
            l += 1
        elif (height[r] < height[l]):
            r -= 1
    return max_area


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(height))


main()
