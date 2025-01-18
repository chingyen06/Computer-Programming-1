def checkComputeRule(school, rule):
    check = 0

    for i in rule:
        ok = 1
        for j in i:
            if (school.count(j) == 0):
                ok = 0
        check += ok
    
    return check

def checkContainRule(school, rule):
    t = 0

    for i in rule:
        for j in i:
            if (school.count(j)):
                t += 1

    return t

def main():
    n = int(input())
    school = list()

    for i in range(n):
        school.append(input().split())

    m = int(input())
    out = [[], []]

    for i in range(m):
        properties = list()
        p1 = input().split(' + ')

        for j in p1:
            properties.append(j.split())

        tempout = list()

        for j in school:
            a = checkComputeRule(j, properties)

            if (a != 0):
                tempout.append(j[0])
        
        out[0].append(tempout)

        tempout = []

        for j in school:
            a = checkContainRule(j, properties)

            tempout.append([j[0], a])

        a = sorted(tempout, key = lambda x: x[1], reverse=True)
        tempout2 = list()

        for j in a:
            if (j[1] < a[0][1]):
                break

            tempout2.append(j[0])

        out[1].append(tempout2)

        #print(out[0], out[1])

    b = int(input())

    for i in out[b]:
        for j in i:
            print(j, end=' ')
        print()

main()