def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    lst = [True if (i + extraCandies >= max_candies) else False for i in candies]
    return lst

def main():
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(kidsWithCandies(candies, extraCandies))

main()