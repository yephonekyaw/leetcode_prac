def longestCommonSubsequence(text1, text2):
    if len(text2) > len(text1):
        text1, text2 = text2, text1
    c = [0 for _ in range(len(text2))]
    for i in range(len(text1)):
        for j in range(len(text2)):
            cur_diag = 0 if i == 0 or j == 0 else prev_diag
            top = 0 if i == 0 else c[j]
            left = 0 if j == 0 else c[j - 1]
            prev_diag = c[j]
            if text1[i] == text2[j]:
                c[j] = cur_diag + 1
            else:
                c[j] = max(top, left)
    return c[len(text2) - 1]


if __name__ == "__main__":
    text1 = ""
    text2 = ""
    print(longestCommonSubsequence(text1, text2))
