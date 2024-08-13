def combinationSum3(k, n):
    pairs = []
    
    def find_pairs(lst, start):
        if len(lst) == k:
            if sum(lst) == n:
                pairs.append([i for i in lst])
        else:
            for num in range(start, 10):
                lst.append(num)
                find_pairs(lst, num + 1)
                lst.pop()

    find_pairs([], 1)
    return pairs

def main():
    k = 4
    n = 1
    print(combinationSum3(k, n))

main()