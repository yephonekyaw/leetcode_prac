import re

def reverseWords(s):
    s = s.strip()
    word_lst = re.split(r"\s+", s)
    for i in range(len(word_lst) // 2):
        word_lst[i], word_lst[len(word_lst) - 1 - i] = word_lst[len(word_lst) - 1 - i], word_lst[i]
    return " ".join(word_lst)


def main():
    s = "  hello world lol "
    print(reverseWords(s))

main()