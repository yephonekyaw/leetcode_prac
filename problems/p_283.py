def moveZeros(nums):
    l, r = 0, 0
    while r < len(nums):
        while l < r and nums[l] != 0:
            l += 1
        while r < len(nums) and nums[r] == 0:
            r += 1
        if l < r and r < len(nums):
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        r += 1
    return nums

def main():
    nums = [0,1,0,3,12]
    print(moveZeros(nums))

main()