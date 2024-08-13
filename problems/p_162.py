def findPeakElement(nums):
    """
            0   1   2   3   4   5   6

        6                       6   
        5                   5       
        4                           4                                                
        3               3   
        2       2           
        1   1       1

        l = 0, r = 6, m = 3
        3 < 5: peak is in the right side => l = m + 1

        l = 4, r = 6, m = 5
        6 > 4: peak is in the left side => r = m

        l = 4, r = 5, m = 4
        5 < 6: peak is in the right side => l = m + 1
        
        l = 5, r = 5, m = 5
        6 > 4: peak is in the left side => r = m
        while l < r

            0   1   2   3   4   5
        
        6                       6
        5                   5
        4               4
        3           3
        2       2
        1   1

        l = 0, r = 5, m = 2
        3 < 4 => ascending: peak is in the right for sure => l = m + 1

        l = 3, r = 5, m = 4
        5 < 6 => ascending: peak is in the right for sure => l = m + 1

        l = 5, r = 5, m = ?
        while l < r is False, so return l
    """
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        # m is in ascending path, so peak is in the right for sure
        if nums[m] < nums[m + 1]:
            l = m + 1
        # m is in descending path, so peak is in the left for sure
        elif nums[m] > nums[m + 1]:
            r = m
    return l

def main():
    nums = [1,2,1,3,5,6,4]
    print(findPeakElement(nums))

main()