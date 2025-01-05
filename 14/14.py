def strike(point):
    if (point == 10):
        return point, 2
    return point, 0

def spare(previousPoint, point):
    if (previousPoint + point == 10):
        return point, 1
    return point, 0

def gameInput(t, addPoint):
    a = strike(int(input()))
    b = [0, 0]

    if (a[1] == 0):
        b = spare(a[0], int(input()))

    if (addPoint == 1):
        t += 2 * a[0] + b[0]
        addPoint -= 1
    elif (addPoint == 2):
        t += 2 * (a[0] + b[0])
        addPoint -= 2
    else:
        t += a[0] + b[0]

    addPoint += a[1] + b[1]

    return t, addPoint

def main():
    t = 0
    addPoint = 0

    for i in range(10):
        a = gameInput(t, addPoint)
        t = a[0]
        addPoint = a[1]

    for i in range(addPoint):
        t += int(input())

    print(t)


if __name__ == "__main__":
    main()
