def decodeString(s):
    stack = []
    for ch in s:
        if ch != "]":
            stack.append(ch)
        else:
            seq = ""
            while stack and stack[-1] != "[":
                seq = stack.pop() + seq
            # remove the open bracket
            stack.pop()

            freq = ""
            while stack and stack[-1].isdigit():
                freq = stack.pop() + freq
                
            stack.append(seq * int(freq))
    
    return "".join(stack)

def main():
    s = "100[leetcode]"
    print(decodeString(s))


main()
