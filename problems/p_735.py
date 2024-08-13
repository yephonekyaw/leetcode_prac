def asteroidCollision(asteroids):
    if not asteroids:
        return []
    stack = []
    stack.append(asteroids[0])

    for i in range(1, len(asteroids)):
        if asteroids[i] > 0:
            stack.append(asteroids[i])
        else:
            while stack and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                stack.pop()
            if stack:
                if stack[-1] > 0 and stack[-1] == abs(asteroids[i]):
                    stack.pop()
                elif stack[-1] < 0:
                    stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])
    return stack


def main():
    asteroids = [-2, 1, -1, -2]
    print(asteroidCollision(asteroids))


main()
