def checkError(card):
    cardDefined = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    colorDefined = ['S', 'H', 'D', 'C']

    for i in card:
        if (i[1:] not in cardDefined or i[0] not in colorDefined):
            return 1
        
    return 0

def checkStraight(card):
    specialRule = [[1, 10, 11, 12, 13], [1, 2, 11, 12, 13], [1, 2, 3, 12, 13], [1, 2, 3, 4, 13]]
    decode = ['A', 1, 'J', 11, 'Q', 12, 'K', 13]
    
    ok = 1
    newCard = list()

    for i in range(0, 5):
        if (card[i][1:] in decode):
            newCard.append(decode[decode.index(card[i][1:])+1])
        else:
            newCard.append(int(card[i][1:]))

    newCard = sorted(newCard)

    if (newCard in specialRule):
        return 1

    for i in range(1, 5):
        if (newCard[i] != newCard[i-1] + 1):
            ok = 0

    return ok


def getNumber(card):
    get = 1

    numberCard = [i[1:] for i in card]
    setNumberCard = set(numberCard)
    countNumber = max(numberCard, key=numberCard.count)

    colorCard = [i[0] for i in card]
    countColor = max(colorCard, key=colorCard.count)

    if (numberCard.count(countNumber) == 2):
        get = 2

    if (len(setNumberCard) == 3):
        get = 3

    if (numberCard.count(countNumber) == 3):
        get = 4

    if (checkStraight(card)):
        get = 5

    if (colorCard.count(countColor) == 5):
        get = 6

    if (len(setNumberCard) == 2):
        get = 7

    if (numberCard.count(countNumber) == 4):
        get = 8

    if (colorCard.count(countColor) == 5 and checkStraight(card)):
        get = 9

    return get

def getPoint(card, tableCard):
    point = list()

    for i in range(2):
        point.append(getNumber([card[i]]+tableCard[0:4]))
    
    point.append(getNumber(card+tableCard[0:3]))
    point.append(getNumber(card+tableCard[1:4]))
    point.append(getNumber(card+tableCard[0:2]+[tableCard[3]]))
    point.append(getNumber(card+tableCard[2:4]+[tableCard[0]]))
    
    return max(point)

def main():
    aCard = input().split(' ')
    bCard = input().split(' ')
    tableCard = input().split(' ')
    aPoint, bPoint = 1, 1
    error = 0
    card = aCard + bCard + tableCard
    setCard = set(card)

    error = error + checkError(aCard) + checkError(bCard) + checkError(tableCard)

    if (error != 0):
        print("Error input")
    elif (len(setCard) != len(card)):
        print("Duplicate deal")
        error = 1

    if (error == 0):
        aPoint = getPoint(aCard, tableCard)
        bPoint = getPoint(bCard, tableCard)
        
        if (aPoint > bPoint):
            print("A %d" %aPoint)
        elif (aPoint < bPoint):
            print("B %d" %bPoint)
        else:
            print("Tie")

main()