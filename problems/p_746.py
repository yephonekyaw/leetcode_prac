def minCostClimbingStairs(cost):
    """
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        
        the idea is to think how it takes to reach a certain level, (0-indexed)
        to reach a certain level i, there are always two ways: sum of i and i - 1
                                                               sum of i and i - 2
        lvl 0 and 1 are the starting point
        lvl 2: min(2 + 1, 2 + 0) => min(101, 2) => 1, 100, 2, 1, 1, 100, 1, 1, 100, 1

        lvl 3: min(3 + 2, 3 + 1) => min(3, 101) => 1, 100, 2, 3, 1, 100, 1, 1, 100, 1

        lvl 4: min(4 + 3, 4 + 2) => min(4, 3) => 1, 100, 2, 3, 3, 100, 1, 1, 100, 1
    """
    lvl = len(cost)
    if lvl <= 1:
        return 0
    elif lvl == 2:
        return min(cost[0], cost[1])
    else:
        cost.append(0)
        for i in range(2, lvl + 1):
            cost[i] += min(cost[i - 1], cost[i - 2])
    return cost[lvl]


def main():
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(minCostClimbingStairs(cost))


main()
