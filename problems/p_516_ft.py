def longestPalindromeSubseq(s):
    l = len(s)
    dp = [0 for _ in range(l)]
    for i in range(l - 1, -1, -1):
        for j in range(l):
            cur_diag = 0 if i == l - 1 or j == 0 else prev_diag
            top = 0 if i == l - 1 else dp[j]
            left = 0 if j == 0 else dp[j - 1]
            prev_diag = dp[j]
            if s[i] == s[j]:
                dp[j] = cur_diag + 1
            else:
                dp[j] = max(top, left)
    return dp[-1]


if __name__ == "__main__":
    s = "babbbbaabb"
    print(longestPalindromeSubseq(s))
