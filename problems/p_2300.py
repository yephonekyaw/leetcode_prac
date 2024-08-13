def successfulPairs(spells, potions, success):
    res = [0] * len(spells)
    potions = sorted(potions)

    def binary_search(spell):
        """
            1 2 2 2 3 4 5, success = 10

            spell = 5, l = 0, r = 6, m = 3
            5 * 2 == 10, l = 0, r = m - 1

            spell = 5, l = 0, r = 2, m = 1
            5 * 2 == 10, l = 0, r = m - 1

            spell = 5, l = 0, r = 1, m = 0

        """
        l, r, first = 0, len(potions) - 1, None
        while l <= r:
            m = (l + r) // 2
            if potions[m] * spell >= success:
                first = m
                r = m - 1
            else:
                l = m + 1
        return len(potions) - first

    for i in range(len(spells)):
        res[i] += binary_search(spells[i]) if potions[-1] * spells[i] >= success else 0

    return res

def main():
    spells = [5,1,3]
    potions = [1, 2, 2, 2, 3, 4, 5]
    success = 10
    print(successfulPairs(spells, potions, success))

main()