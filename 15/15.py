def countBmi():
    information = list(map(float, input().split(' ')))

    bmi = information[1] / (information[0] ** 2)

    if (bmi * 1000 % 10 == 5):
        if (bmi * 100 % 10 % 2 == 0):
            bmi += 0.001
        else:
            bmi -= 0.001
    
    bmi = round(bmi, 2)

    return bmi

def main():
    n = int(input())
    t = 0
    bmi = list()

    for i in range(n):
        bmi.append(countBmi())
        t += 1
    
    bmi = sorted(bmi)

    print("%.2f" %bmi[t-1])
    print("%.2f" %bmi[0])
    if (t % 2 == 0):
        print("%.2f" %((bmi[t//2-1]+bmi[t//2]) / 2 * 100//100))
    else:
        print("%.2f" %bmi[t//2])
    print("%.2f" %max(bmi, key=bmi.count))

main()