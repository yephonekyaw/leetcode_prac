def longestPalindromeSubseqTopDown(s):
    dp = [[-float("inf") for _ in range(len(s))] for _ in range(len(s))]

    def search(fr, to):
        if dp[fr][to] != -float("inf"):
            return dp[fr][to]

        if fr == to:
            dp[fr][to] = 1
        elif to - fr + 1 == 2 and s[fr] == s[to]:
            dp[fr][to] = 2
        elif s[fr] == s[to]:
            dp[fr][to] = 2 + search(fr + 1, to - 1)
        else:
            dp[fr][to] = max(search(fr, to - 1), search(fr + 1, to))

        return dp[fr][to]

    return search(0, len(s) - 1)


def longestPalindromeSubseqBottomUp(s: str) -> int:
    n = len(s)
    dp = [[0] * (n) for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for l in range(2, n + 1):
        for i in range(0, n - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]


if __name__ == "__main__":
    s = "aacabdkacaa"
    print(longestPalindromeSubseqBottomUp(s))
