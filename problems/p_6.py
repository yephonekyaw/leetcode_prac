def convert(string, row):
    if row == 1 or row > len(string):
        return string

    res, i, j = "", (row - 1) * 2, 0
    for k in range(row):
        cur = k
        res += string[cur]
        while cur < len(string):
            if i != 0 and cur + i < len(string):
                res += string[cur + i]
            cur += i

            if j != 0 and cur + j < len(string):
                res += string[cur + j]
            cur += j

        i -= 2
        j += 2

    return res


if __name__ == "__main__":
    string = "P"
    row = 2
    print(convert(string, row))
