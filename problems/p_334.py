def increasingTriplet(nums):
    a = b = float('inf')
    for num in nums:
        if num <= a:
            a = num
        elif num <= b:
            b = num
        else:
            return True
    return False

def main():
    nums = [2, 1, 5, 0, 4, 6]
    print(increasingTriplet(nums))

main()