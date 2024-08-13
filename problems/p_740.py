def deleteAndEarn(nums):
    unique = list(set(nums))
    count_dict = {i: nums.count(i) * i for i in unique}
    fr_earn, nd_earn = 0, 0
    for i in range(len(unique)):
        cur_earn = count_dict.get(unique[i])
        if i > 0 and unique[i - 1] + 1 == unique[i]:
            tmp = nd_earn
            nd_earn = max(cur_earn + fr_earn, nd_earn)
            fr_earn = tmp
        else:
            tmp = nd_earn
            nd_earn += cur_earn
            fr_earn = tmp
    return nd_earn

    # if len(unique) == 1:
    #     return count_dict.get(unique[0])

    # for i in range(1, len(unique)):
    #     key = unique[i]
    #     if unique[i - 1] == key - 1:
    #         count_dict[key] = max(count_dict.get(key) + (count_dict.get(unique[i - 2]) if i - 2 >= 0 else 0), count_dict.get(key - 1))
    #     else:
    #         count_dict[key] = count_dict.get(key) + count_dict.get(unique[i - 1])
    # return count_dict.get(unique[-1])

def main():
    nums = [3, 4, 2]
    print(deleteAndEarn(nums))

main()