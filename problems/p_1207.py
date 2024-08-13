def uniqueOccurrences(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    freq_arr = list(freq.values())
    return len(freq_arr) == len(set(freq_arr))

def main():
    arr = [1,2]
    print(uniqueOccurrences(arr))

main()