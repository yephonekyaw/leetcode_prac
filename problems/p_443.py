def compress(chars):
    left, right, current = 0, 0, 0
    while right < len(chars):
        if chars[left] == chars[right]:
            right += 1
        else:
            chars[current] = chars[left]
            current += 1
            if right - left > 1:
                for c in str(right - left):
                    chars[current] = c
                    current += 1
            left = right
    
    chars[current] = chars[left]
    current += 1
    if (right - left > 1):
        for c in str(right - left):
            chars[current] = c
            current += 1
    
    return current

def main():
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(compress(chars))

main()