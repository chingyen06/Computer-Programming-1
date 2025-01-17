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
        n = input()
        t = 0

        if (n == '-1'):
            break

        n = binaryToDecimal(n)

        for i in range(n+1):
            c = int(circuit(i))

            if (c >= 1):
                c = c - 1

            t = t + c

        print(decimalToBinary(t).zfill(14))

main()