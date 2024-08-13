def main():
    rand = 2
    pick = 2
    def guess(num):
        return -1 if num > pick else 1 if num < pick else 0

    def guessNumber(n: int) -> int:
        l = 1
        r = n
        while True:
            m = (l + r) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res == -1:
                r = m - 1
            else:
                l = m + 1
    
    print(guessNumber(rand))

main()