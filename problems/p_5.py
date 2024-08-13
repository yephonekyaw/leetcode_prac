import pprint


def longestPalindrome(s: str) -> str:
    dp = [[True if i == j else False for j in range(len(s))] for i in range(len(s))]
    init, size = 0, 1
    # for size 2, it is a bit different
    for i in range(0, len(s) - 2 + 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            size = 2
            init = i

    for l in range(3, len(s) + 1):
        for i in range(0, len(s) - l + 1):
            j = l + i - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                size = max(size, l)
                init = i
    return s[init : init + size]


"""
        0   1   2   3   4   5   6   7
        a   b   a   c   d   a   b   a

0   a   1   0   1   0   0   0   0   0
1   b   0   1   0   0   0   0   0   0
2   a   0   0   1   0   0   0   0   0
3   c   0   0   0   1   0   0   0   0
4   d   0   0   0   0   1   0   0   0
5   a   0   0   0   0   0   1   0   1
6   b   0   0   0   0   0   0   1   0
7   a   0   0   0   0   0   0   0   1

"""
if __name__ == "__main__":
    s = "forgeeksskeegfor"
    print(longestPalindrome(s))
