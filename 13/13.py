length = list()

def position():
    x = input().split(' ')
    x = list(map(int, x))

    for i in range(x[0], x[1]):
        length[i+20] = 1

    return 0

def main():
    t = 0

    for i in range(41):
        length.append(0)

    for i in range(int(input())):
        position()

    for i in range(41):
        if (length[i] == 1):
            t = t + 1

    print(t)

if __name__ == "__main__":
    main()
