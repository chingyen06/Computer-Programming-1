def grayCode(n, k):
    if (n == 1):
        return str(k)
    elif (k < 2 ** (n-1)):
        return "0" + grayCode(n-1, k)
    else:
        return "1" + grayCode(n-1, 2 ** n - 1 - k)

def main():
    while (True):
        inputNK = list(map(int, input().split()))

        if (inputNK[0] == -1):
            break

        print(grayCode(inputNK[0], inputNK[1]))

main()