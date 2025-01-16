def pairs(s, d):
    defined = [['(', '[', '{'], [')', ']', '}']]
    previous = list()
    realDepth = 0
    word = ''

    for i in s:
        if (realDepth == d):
            if (i not in defined[0] and i not in defined[1]):
                word = word + i
        if (i in defined[0]):
            previous.append(defined[1][defined[0].index(i)])
            realDepth = realDepth + 1
        elif (i in defined[1]):
            if (len(previous) == 0):
                print("fail")
                return 0
            if (i != previous[-1]):
                print("fail")
                return 0
            else:
                previous.pop(-1)
                realDepth = realDepth - 1

    if (len(previous) == 0):
        if (word == ''):
            print("pass, EMPTY")
        else:
            print("pass,", word)
    else:
        print("fail")


def main():
    n, d = int(input()), int(input())

    for i in range(n):
        s = input()

        pairs(s, d)

main()