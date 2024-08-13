import math

def bulbSwitch(n: int) -> int:
    return math.ceil(math.sqrt(n + 1) - 1)

def main():
    n = 3
    print(bulbSwitch(3))

main()