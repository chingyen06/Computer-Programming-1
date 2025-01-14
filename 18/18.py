def equilateralTriangle(t, n):
    for i in range(t-1-n):
        print("#", end='')
    for i in range(2*n+1):
        print("*", end='')
    for i in range(t-1-n):
        print("#", end='')
    print()

def invertedTriangle(t, n):
    for i in range(n):
        print("#", end='')
    for i in range(2*(t-n-1)+1):
        print("*", end='')
    for i in range(n):
        print("#", end='')
    print()

def diamond(t, n):
    a = t // 2

    if (n <= a):
        for i in range(a-n):
            print(" ", end='')
        for i in range(2*n+1):
            print("*", end='')
        for i in range(a-n):
            print(" ", end='')
    else:
        for i in range(n-a):
            print(" ", end='')
        for i in range(2*(t-n-1)+1):
            print("*", end='')
        for i in range(n-a):
            print(" ", end='')
    print()

def fish(t, n):
    a = t // 2

    if (n <= a):
        for i in range(a-n):
            print(" ", end='')
        for i in range(2*n+1):
            print("*", end='')
        for i in range((a-n)*2):
            print(" ", end='')
        for i in range(n):
            print("-", end='')
    else:
        for i in range(n-a):
            print(" ", end='')
        for i in range(2*(t-n-1)+1):
            print("*", end='')
        for i in range((n-a)*2):
            print(" ", end='')
        for i in range(t-n-1):
            print("-", end='')
    print()

def main():
    c, n = int(input()), int(input())

    if (n % 2 == 0 or n <= 2 or n >= 50):
        print("error")
        return None
    if (c == 1):
        for i in range(n):
            equilateralTriangle(n, i)
    elif (c == 2):
        for i in range(n):
            invertedTriangle(n, i)
    elif (c == 3):
        for i in range(n):
            diamond(n, i)
    else:
        for i in range(n):
            fish(n, i)

main()