def findDifference(nums1, nums2):
    num_loc = {}
    for i in range(max(len(nums1), len(nums2))):
        if i < len(nums1):
            item = nums1[i]
            loc = num_loc.get(item)
            if loc == None:
                num_loc[item] = 1
            elif loc == 2:
                num_loc[item] = 10
        
        if i < len(nums2):
            item = nums2[i]
            loc = num_loc.get(item)
            if loc == None:
                num_loc[item] = 2
            elif loc == 1:
                num_loc[item] = 10
    
    disti_loc = [[], []]
    for k in num_loc.keys():
        if num_loc.get(k) == 1:
            disti_loc[0].append(k)
        elif num_loc.get(k) == 2:
            disti_loc[1].append(k)

    return disti_loc

def main():
    nums1 = [26,48,-78,-25,42,-8,94,-68,26]
    nums2 = [61,-17]
    print(findDifference(nums1, nums2))

main()