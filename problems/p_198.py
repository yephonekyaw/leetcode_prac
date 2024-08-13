def rob(nums):
    num_of_house = len(nums)
    memoi = [0] * num_of_house
    if num_of_house <= 2:
        return max(nums)
    else:
        memoi[0], memoi[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, num_of_house):
            memoi[i] = max(memoi[i - 2] + nums[i], memoi[i - 1])
    return memoi[num_of_house - 1]
    """
        
    """


def main():
    nums = [1, 2, 3, 1]
    print(rob(nums))

main()