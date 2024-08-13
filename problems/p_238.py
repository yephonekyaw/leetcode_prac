def productExceptSelf(nums):
    zeros_count = 0
    prod = 1
    prod_non_zero = 1
    for i in nums:
        if i == 0:
            zeros_count += 1
        
        if zeros_count > 1:
            return [0] * len(nums)
        
        prod *= i
        prod_non_zero = prod_non_zero * i if i != 0 else prod_non_zero * 1
       
    return [prod // num if num != 0 else prod_non_zero for num in nums]

def main():
    nums = [-1,1,0,-3,3]
    print(productExceptSelf(nums))

main()