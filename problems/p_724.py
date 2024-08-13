def pivotIndex(nums):
    """
        1 8 11 17 22 28

        0: left => 0
           right => prefix[-1] - prefix[i]

        1: left => prefix[i - 1]
           right => prefix[-1] - preifx[i]
    """
    all_sum = 0
    prefix = []
    for num in nums:
        all_sum += num
        prefix.append(all_sum)

    print(prefix)
    for i in range(len(nums)):
        if i == 0 and prefix[-1] - prefix[i] == 0:
            return i
        elif i == len(nums) - 1 and prefix[i - 1] == 0:
            return i
        elif i != 0 and i != len(nums) - 1 and prefix[i - 1] == prefix[-1] - prefix[i]:
            return i

    return -1

def main():
    nums = [0,-1,-1,-1,-1,-1]
    print(pivotIndex(nums))


main()
