def fullJustify(words, maxWidth):
    res = []
    line, length = [], 0
    i = 0

    while i < len(words):
        if length + len(line) + len(words[i]) > maxWidth:
            # Line complete
            extra_space = maxWidth - length
            # if line has only one element, 1 - 1 will be 0
            spaces = extra_space // max(1, len(line) - 1)
            remainder = extra_space % max(1, len(line) - 1)

            for j in range(max(1, len(line) - 1)):
                line[j] += " " * spaces
                if remainder:
                    line[j] += " "
                    remainder -= 1
            res.append("".join(line))
            line, length = [], 0  # Reset line and length

        line.append(words[i])
        length += len(words[i])
        i += 1

    # Handle last line
    last_line = " ".join(line)
    trail_space = maxWidth - len(last_line)
    res.append(last_line + " " * trail_space)

    return res


def run_algo(words, maxWidth):
    print("\n".join(fullJustify(words, maxWidth)))


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    run_algo(words, maxWidth)
