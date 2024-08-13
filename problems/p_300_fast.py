def lengthOfLIS(nums):
    dp = [1 for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

if __name__ == '__main__':
    nums = [1,3,6,7,9,4,10,5,6]
    print(f'Length is {lengthOfLIS(nums)}')