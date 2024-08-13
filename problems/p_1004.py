from collections import deque


def longestOnes(nums, k):
    max_count = -float('inf')
    l, r, zero_count = 0, 0, 0
    while r < len(nums):
        if nums[r] == 0:
            zero_count += 1
        
        while zero_count > k:
            if nums[l] == 0:
                zero_count -= 1
            l += 1
        
        max_count = max(max_count, r - l + 1)
        r += 1
    return max_count
            
                

def main():
    nums = [0,0,1,1,1,0,0]
    k = 0
    print(longestOnes(nums, k))


"""
    0 1 2 3 4 5 6 7 8 9 10
    0 0 1 1 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1, k = 3
    1 1 1 1 1 => 5
    0 1 1 1 1 1 1 1 1 => 8
    0 0 1 1 1 1 1 1 1 1 1 1 => 10
"""


main()
