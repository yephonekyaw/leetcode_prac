def nthSuperUglyNumber(n, primes) -> int:
    factors, k = primes, len(primes)
    starts, ugly_num = [0] * k, [1]
    for _ in range(n - 1):
        candidates = [factors[i] * ugly_num[starts[i]] for i in range(k)]
        new_num = min(candidates)
        ugly_num.append(new_num)
        starts = [starts[i] + (new_num == candidates[i]) for i in range(k)]

    return ugly_num[-1]

if __name__ == '__main__':
    n = 12
    print(nthSuperUglyNumber(n, primes=[2, 7, 13, 19]))
