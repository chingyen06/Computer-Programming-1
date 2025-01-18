circle = list()

def bingo(s):
    global circle

    for i in range(len(circle)):
        for j in range(len(s)):
            if (circle[i] == s[j]):
                #print(circle[i], j)
                s[j] = -1

    #print(s)

    for i in range(len(s)):
        if (s[i] != -1):
            s[i] = -2

    '''print(s)
    print("=====")'''

    return s

def rowLine(n, s):
    global circle

    correct = 0
    for i in range(n):
        add = 1
        for j in range(n):
            if (s[i*n+j] == -2):
                add = 0
        correct += add

    #print(correct)

    return correct

def columnLine(n, s):
    global circle

    correct = 0
    for i in range(n):
        add = 1
        for j in range(n):
            if (s[j*n+i] == -2):
                add = 0
        correct += add

    #print(correct)

    return correct

def slopeLine(n, s):
    global circle

    correct = 0

    add = 1
    for i in range(n):
        if (s[i*(n+1)] == -2):
            add = 0
    correct += add

    add = 1
    for i in range(n):
        if (s[(n-1)+i*(n-1)] == -2):
            add = 0
    correct += add

    #print(correct)

    return correct

def main():
    global circle
    n, m = int(input()), int(input())
    A, B = list(map(int, input().split())), list(map(int, input().split()))

    circle = list(map(int, input().split()))

    A = bingo(A)
    B = bingo(B)

    '''print(A)
    print(B)'''

    a = rowLine(n, A) + columnLine(n, A) + slopeLine(n, A)
    b = rowLine(n, B) + columnLine(n, B) + slopeLine(n, B)

    if (a > b):
        print("A Win")
    elif (b > a):
        print("B Win")
    else:
        print("Tie")

main()