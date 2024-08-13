def canPlaceFlowers(flowerbed, n):
    for i in range(len(flowerbed)):
        left = True if (
            i > 0 and flowerbed[i - 1] == 0 or i == 0) else False
        right = True if (i < len(flowerbed) -
                         1 and flowerbed[i + 1] == 0 or i == len(flowerbed) - 1) else False
        if (left and right and flowerbed[i] != 1 and n != 0):
            flowerbed[i] = 1
            i += 1
            n -= 1
        if (n == 0):
            break

    return True if (n == 0) else False


def main():
    flowerbed = [0,0,0,0,0,1,0,0]
    n = 0
    print(canPlaceFlowers(flowerbed, n))


main()
