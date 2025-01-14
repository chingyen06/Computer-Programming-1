def rightTriangle(n):
    for i in range(1, n):
        print(i, end='')
    for i in range(n, 0, -1):
        print(i, end='')

def equilateralTriangle(t, n):
    for i in range(t-n):
        print("_", end='')
    rightTriangle(n)
    for i in range(t-n):
        print("_", end='')

def invertedTriangle(t, n):
    for i in range(n-1):
        print("_", end='')
    for i in range(1, t-n+2):
        print(i, end='')
    for i in range(t-n, 0, -1):
        print(i, end='')
    for i in range(n-1):
        print("_", end='')

def main():
    m, n = int(input()), int(input())

    if (m == 1):
        for i in range(1, n+1):
            rightTriangle(i)
            print()
    elif (m == 2):
        for i in range(1, n+1):
            equilateralTriangle(n, i)
            print()
    else:
        for i in range(1, n+1):
            invertedTriangle(n, i)
            print()

main()