cave = list()
MaxGold = 0

def findCave(number):
    global cave

    for i in range(len(cave)):
        if (cave[i][0] == number):
            return i

def dfs(number, gold, visit):
    global cave, MaxGold

    location = findCave(number)

    if (cave[location][1] == 0 or location in visit):
        if (gold > MaxGold):
            MaxGold = gold
        return 0
    
    dfs(cave[location][2], gold + cave[location][1], visit + [location])
    dfs(cave[location][3], gold + cave[location][1], visit + [location])

def main():
    info = list(map(int, input().split()))

    for i in range(info[0]):
        cave.append(list(map(int, input().split())))

    dfs(info[1], 0, [])

    print(MaxGold)

main()
