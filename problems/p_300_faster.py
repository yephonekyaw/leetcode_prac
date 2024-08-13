def binary_search(sorted_dp: list, num: int) -> int:
    f, l = 0, len(sorted_dp) - 1
    while f <= l:
        m = (f + l) // 2
        if sorted_dp[m] == num:
            return m
        elif sorted_dp[m] < num:
            f = m + 1
        else:
            l = m - 1
    return f


def lengthOfLIS(nums):
    size = -float("inf")
    dp = [-float("inf") if i == 0 else float("inf") for i in range(len(nums) + 1)]
    for i in range(len(nums)):
        pos = binary_search(dp, nums[i])
        if dp[pos - 1] < nums[i] and nums[i] < dp[pos]:
            dp[pos] = nums[i]
            size = max(size, pos)
    return size


if __name__ == "__main__":
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print(f"Length is {lengthOfLIS(nums)}")
