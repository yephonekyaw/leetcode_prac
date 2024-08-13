def findMaxAverage(nums, k):
    total = sum(nums[0:k])
    avg = total / k
    for i in range(1, len(nums) - k + 1):
        total = total - nums[i - 1] + nums[i + k - 1]
        if (avg < total / k):
            avg = total / k
    return avg


def main():
    nums = [5]
    k = 1
    print(findMaxAverage(nums, k))


main()
