import math

def main():
    n = int(input())
    location, distance = list(), list()

    for i in range(n):
        location.append(list(map(int, input().split())))

    for i in location:
        for j in location:
            if (i < j):
                distance.append([i[0], j[0], math.sqrt((i[1]-j[1]) ** 2 + (i[2]-j[2]) ** 2 + (i[3]-j[3]) ** 2)])
    
    distance = sorted(distance, key = lambda x:x[2])
    
    #print(location)
    #print(distance)

    count = 0

    for i in distance:
        if (count >= 3):
            break

        locationA = "{0} {1} {2}".format(location[i[0]-1][1], location[i[0]-1][2], location[i[0]-1][3])
        locationB = "{0} {1} {2}".format(location[i[1]-1][1], location[i[1]-1][2], location[i[1]-1][3])

        print(i[0], i[1], locationA, locationB)

        count += 1


main()