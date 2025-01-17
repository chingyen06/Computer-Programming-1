def binaryToDecimal(binary):
    decimal = 0

    for i in range(len(binary)):
        decimal = decimal + int(binary[i]) * (2 ** (len(binary) - i - 1))

    return decimal

def decimalToBinary(decimal):
    result = bin(decimal).replace("0b", "")
    zero = ""

    for i in range(4 - len(result)):
        zero = zero + "0"
 
    result = zero + result

    return result

def circuit(m):
    if (m == 0 or m == 1):
        return m
    elif (m % 2 == 0):
        return 1 + circuit(m/2)
    else:
        return 1 + circuit((m+1)/2)

def main():
    while (True):
        n, a = input(), input()

        n = binaryToDecimal(n)

        c = int(circuit(n))

        if (c >= 1):
            c = c - 1

        print(decimalToBinary(c))

        if (a == '-1'):
            break

main()