def main():
    n, t, a, b, c, d = int(input()), int(input()), int(input()), float(input()), int(input()), float(input())
    total = a
    cured = list()

    print(1, a, a, 0)
    cured.append([0, a])

    for i in range(1, t):
        x = (b / c) * (1 - d)

        infect = int(a*x)
        canInfect = int(n*(1-d)) - a
        if (infect > canInfect):
            if (canInfect > 0):
                infect = canInfect
            else:
                infect = 0
        
        a = a + infect
        cured.append([i, infect])

        if (len(cured) > 0 and i == cured[0][0] + c):
            a = a - cured[0][1]
            print(i+1, a, infect, cured[0][1])
            d = d + cured[0][1] / n
            cured.pop(0)
        else:
            print(i+1, a, infect, 0)

        total = total + infect

    print(total)

main()