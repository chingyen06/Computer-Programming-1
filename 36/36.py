connect = dict()

def findPath(start, end, rest):
    stopPath, stop = list(), -1
    queue = [[start, [start]]]
    visited = list()
    findRest = False

    while (queue and findRest == False):
        now = queue.pop(0)
        visited.append(now[0])
        node, path = now[0], now[1]

        if (node == end):

            for i in rest:
                if (i in path):
                    findRest = True
                    stop = i
                    break
            
            if (findRest == True):
                stopPath = path
        
        if (node == end):
            continue
        
        for i in connect[node]:
            if (i not in visited):
                queue.append([i, path+[i]])

    return stopPath, stop

def main():
    n, start, end = list(map(int, input().split()))
    rest = list(map(int, input().split()))

    for i in range(n):
        a = list(map(int, input().split()))

        if (a[0] not in connect):
            connect[a[0]] = list()
        if (a[1] not in connect):
            connect[a[1]] = list()
        
        connect[a[0]].append(a[1])
        connect[a[1]].append(a[0])

    path, stop = findPath(start, end, rest)

    if (stop != -1):
        print(stop)
        for i in path:
            print(i, end=' ')
    else:
        print("NO")

main()