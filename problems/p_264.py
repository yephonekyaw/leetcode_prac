def nthUglyNumber(n: int) -> int:
        if n == 1:
            return 1
        
        result = [0] * n
        result[0] = 1
        i_two = 0
        i_three = 0
        i_five = 0

        for i in range(1, n):
            two_next = result[i_two] * 2
            three_next = result[i_three] * 3
            five_next = result[i_five] * 5
            min_next = min(two_next, three_next, five_next)
            if two_next == min_next:
                i_two += 1
            if three_next == min_next:
                i_three += 1
            if five_next == min_next:
                i_five += 1
            result[i] = min_next

        return result[n - 1]

if __name__ == '__main__':
    n = 11
    print(nthUglyNumber(n))
