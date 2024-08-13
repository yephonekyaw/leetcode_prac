def longestSubarray(nums):
    k = 1
    l, r = 0, 0
    zero_count, max_count = 0, -float('inf')
    while r < len(nums):
        if nums[r] == 0:
            zero_count += 1
        
        while zero_count > k:
            if nums[l] == 0:
                zero_count -= 1
            l += 1
        
        max_count = max(max_count, r - l)
        r += 1
    return max_count

def main():
    nums = [1,1,1]
    print(longestSubarray(nums))


main()