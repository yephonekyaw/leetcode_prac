def isSubsequence(s, t):
    x, y = 0, 0
    while x < len(s) and y < len(t):
        if s[x] == t[y]:
            x = x + 1
        y = y + 1

        if x == len(s):
            break
        
    return True if x == len(s) else False

def main():
    s = "axc"
    t = "ahbgdc"
    print(isSubsequence(s, t))


main()
