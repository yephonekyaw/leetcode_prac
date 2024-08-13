from collections import deque

def removeStars(s):
    st = deque()
    for ch in s:
        if ch == '*':
            st.pop()
            continue
        st.append(ch)
    
    return "".join(st)

def main():
    s = "erase*****"
    print(removeStars(s))

main()