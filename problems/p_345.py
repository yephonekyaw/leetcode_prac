def reverseVowels(s):
    left, right, vowels = 0, len(s) - 1, "aeiou"
    s_lst = list(s)
    while(left < right):
        while left < right and s_lst[left].lower() not in vowels:
            left += 1
        while left < right and s_lst[right].lower() not in vowels:
            right -= 1
        
        if left < right:
            s_lst[left], s_lst[right] = s_lst[right], s_lst[left]
            left, right = left + 1, right - 1
        
    return "".join(s_lst)
    
def main():
    s = "Sore was I ere I saw Eros."
    print(reverseVowels(s))

main()