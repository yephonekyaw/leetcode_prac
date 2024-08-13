def tribonacci(n):
    if n <= 1:
        return n
    elif n == 2:
        return 1
    else:
        memoi = [0] * (n + 1)
        memoi[1], memoi[2] = 1, 1
        for i in range(3, n + 1):
            memoi[i] = memoi[i - 3] + memoi[i - 2] + memoi[i - 1]
        return memoi[n]

def main():
    n = 3
    print(tribonacci(n))

main()