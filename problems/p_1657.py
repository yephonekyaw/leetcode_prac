def closeStrings(word1, word2):
    # if any characters are different
    unique1, unique2 = set(word1), set(word2)
    if unique1 != unique2:
        return False

    freq_1 = sorted([word1.count(ch) for ch in unique1])
    freq_2 = sorted([word2.count(ch) for ch in unique2])
    return freq_1 == freq_2

def main():
    word1 = "uau"
    word2 = "ssx"
    print(closeStrings(word1, word2))

main()