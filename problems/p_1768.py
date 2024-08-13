import re

def mergeAlternately(word1: str, word2: str) -> str:
    r = re.compile(r"\s+")
    word1 = r.sub('', word1)
    word2 = r.sub('', word2)
    ans = ""
    for i in range(min(len(word1), len(word2))):
        ans += word1[i] + word2[i]
    
    return ans + ''.join(word1[i + 1:]) + ''.join(word2[i + 1:])

def main():
    word1 = "ab"
    word2 = "pqrs"
    print(mergeAlternately(word1, word2))

main()