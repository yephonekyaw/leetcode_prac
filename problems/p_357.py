import math

def countNumbersWithUniqueDigits(n):
    if n == 0 or n == 1:
        return 10 * n
    
    # for the first digit
    res = 10
    for i in range(2, n + 1):
        # the first cannot start with 0, therefore only 9 digits for the first position
        prod = 9
        for j in range(2, i + 1):
            prod *= (10 - j + 1)
        res += prod
    return res

def main():
    n = 2
    print(countNumbersWithUniqueDigits(n))

main()