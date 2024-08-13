import math

def minEatingSpeed(piles, h):
    # we need to use bineary search on finding the minimum eating speed which
    # ranges within 1 and the max value of all piles
    l, r = 1, max(piles)
    while l <= r:
        m = (l + r) // 2
        required_hr = sum([math.ceil(b / m) for b in piles])
        if required_hr <= h:
            r = m - 1
        else:
            l = m + 1
    return l

    """
        1 2 3 4 5 6 7 8 9 10 11
        [3, 6, 7, 11]

        If the required time is less than the given time, there can still be more optimal eating speed
        in the left region. Howerver, the required time is greater than the given time, surely the solution
        must be in the right region.
        
        l = 1, r = 11, m = 6
        [1, 1, 2, 2] => 6 < 8: not the best yet => r = m - 1

        l = 1, r = 5, m = 3
        [1, 2, 3, 4] => 10 > 8: in the right region => l = m + 1

        l = 4, r = 5, m = 4
        [1, 2, 2, 3] => 8 = 8: not the best yet => r = m - 1

        l = 4, r = 3, m = ?
        return l
    """

def main():
    piles = [30,11,23,4,20]
    h = 6
    print(minEatingSpeed(piles, h))

main()