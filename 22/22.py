def checkError(card):
    cardDefined = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    colorDefined = ['S', 'H', 'D', 'C']

    for i in card:
        if (i[0:-1] not in cardDefined or i[-1] not in colorDefined):
            print("Error input")
            return 1
        
    return 0

def checkStraight(card):
    specialRule = [[1, 10, 11, 12, 13], [1, 2, 11, 12, 13], [1, 2, 3, 12, 13], [1, 2, 3, 4, 13]]
    decode = ['A', 1, 'J', 11, 'Q', 12, 'K', 13]
    
    ok = 1
    newCard = list()

    for i in range(0, 5):
        if (card[i][0:-1] in decode):
            newCard.append(decode[decode.index(card[i][0:-1])+1])
        else:
            newCard.append(int(card[i][0:-1]))

    newCard = sorted(newCard)

    if (newCard in specialRule):
        return 1

    for i in range(1, 5):
        if (newCard[i] != newCard[i-1] + 1):
            ok = 0

    return ok


def getNumber(card):
    get = 1

    numberCard = [i[0:-1] for i in card]
    setNumberCard = set(numberCard)
    countNumber = max(numberCard, key=numberCard.count)

    colorCard = [i[-1] for i in card]
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

def main():
    n = int(input())
    player = list()
    error = 0
    exist = list()

    for i in range(n):
        card = input().split(' ')

        name = card[0]

        card.remove(name)

        error = error + checkError(card)

        for i in card:
            if (i in exist and error == 0):
                print("Duplicate deal")
                error = 1

        exist.extend(card)
        
        if (error == 0):
            player.append([getNumber(card), name])

    if (error == 0):
        player = sorted(player, reverse=True)

        for i in player:
            print("%s %d" %(i[1], i[0]))
        

main()