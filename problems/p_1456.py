def maxVowels(s, k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_count = -float('inf')
    count = 0
    for i in range(len(s)):
        if i < k and s[i] in vowels:
            count += 1
        elif i >= k:
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
        print(i, count)

        if max_count < count:
            max_count = count
    return max_count

def main():
    s = "tryhard"
    k = 4
    print(maxVowels(s, k))

main()