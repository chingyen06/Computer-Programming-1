import math

def getTriangle(a, b, c):
    s = (a + b + c) / 2

    if (a + b <= c or a + c <= b or b + c <= a):
        print("not a triangle")
        return 0
    elif (a == b == c):
        print("equilateral triangle", end='')
    elif ((a == b and a**2 + b**2 > c**2) or (a == c and a**2 + c**2 > b**2) or (b == c and b**2 + c**2 > a**2)):
        print("isosceles triangle", end='')
    elif (c**2 > a**2 + b**2):
        print("obtuse triangle", end='')
    elif (c**2 < a**2 + b**2):
        print("acute triangle", end='')
    elif (c**2 == a**2 + b**2):
        print("right triangle", end='')
    
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def main():
    n = int(input())
    triangle = list()
    area = list()

    for i in range(n):
        triangle = list(map(int, input().split(' ')))
        triangle = sorted(triangle)

        a = getTriangle(triangle[0], triangle[1], triangle[2])

        if (a > 0):
            print(" %.2f" %a)
            area.append(a)

    if (len(area) > 0):
        print("%.2f\n%.2f" %(max(area), min(area)))
    else:
        print("All inputs are not triangles!")

if __name__ == "__main__":
    main()