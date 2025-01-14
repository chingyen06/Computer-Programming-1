def inputCourse():
    course = [input(), int(input())]

    for i in range(course[1]):
        course.append(input())

    return course

def compare(course, now, n):
    t = 0

    for i in range(2, 2 + course[now][1]):
        for j in range(now + 1, n):
            if (j == now):
                continue
            if (course[now][i] in course[j]):
                print("%s,%s,%s" %(course[now][0], course[j][0], course[now][i]))
                t = 1

    return t

def check(course, n):
    defined = ["11", "1c", "21", "2c", "31", "3c", "41", "4c", "51", "5c"]
    t = 0

    for i in range(n):
        for j in range(2, 2 + course[i][1]):
            ok = 0
            for k in range(0, 9, 2):
                if (defined[k] <= course[i][j] <= defined[k+1]):
                    ok = 1
                    break
            if (ok == 0):
                t = -100
            
        if (course[i][1] < 1 or course[i][1] > 3):
            t = -100

    return t


def main():
    n = int(input())
    course = list()
    t = 0

    if (n < 2 or n > 10):
        t = -100

    for i in range(n):
        course.append(inputCourse())

    t = t + check(course, n)

    if (t < 0):
        print(-1)
    else:
        t = 0

        for i in range(n):
            t = t + compare(course, i, n)
        
        if (t == 0):
            print("correct")

    

main()