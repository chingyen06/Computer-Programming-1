def reverseOutput(s):
    for i in range(len(s)-1, -1, -1):
        print(s[i], end='')

def main():
    A, B = input(), input()
    X, Y = input(), input()
    N = abs(len(X) - len(Y))

    C = A + " " + B

    print(C)

    listC = C.split()
    D = ""

    for i in range(len(listC)):
        if (listC[i].lower() == X.lower()):
            listC[i] = Y
        D = D + listC[i] + " "

    print(D)

    noSpaceC, noSpaceD = C.replace(' ', ''), D.replace(' ', '')

    print(len(noSpaceC), len(noSpaceD))

    listD = D.split()

    for i in range(len(listC)):
        if (listD[i] == Y):
            reverseOutput(listD[i])
            print(' ', end='')
        else:
            print(listD[i], end=' ')
    print()

    previous = 0

    for i in range(0, len(C), N):
        if (previous == 2 and C[i] == ' '):
            continue
        print(C[i], end='')
        if (C[i] == ' '):
            previous = previous + 1
        else:
            previous = 0

main()