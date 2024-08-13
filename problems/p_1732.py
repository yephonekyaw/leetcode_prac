def largestAltitude(gain):
    alt = 0
    max_lat = 0
    for g in gain:
        alt += g
        max_lat = max(max_lat, alt)

    return max_lat

def main():
    gain = [-4,-3,-2,-1,4,3,2]
    print(largestAltitude(gain))

main()