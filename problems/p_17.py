def letterCombinations(digits):
    combinations = []
    letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    if len(digits) == 0:
        return combinations

    def combine(seq, index):
        print(seq)
        if len(seq) == len(digits):
            combinations.append("".join(seq))
        else:
            for l in letters.get(digits[index]):
                seq.append(l)
                combine(seq, index + 1)
                seq.pop()
    
    combine([], 0)
    return combinations

def main():
    digits = "234"
    print(letterCombinations(digits))

main()