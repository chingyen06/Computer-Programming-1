def countPoint(card):
    point = ['J', 'Q', 'K']

    for i in range(len(card)):
        if (card[i] in point):
            card[i] = 0.5
        elif (card[i] == 'A'):
            card[i] = 1
        else:
            card[i] = int(card[i])
        
    return card

def countIndexPoint(card):
    point = ['J', 'Q', 'K']

    if (card == 'N'):
        return 0

    if (card in point):
        return 0.5
    
    if (card == 'A'):
        return 1
    
    return int(card)

def main():
    n = int(input())
    bet = list(map(int, input().split(' ')))
    player = countPoint(input().split(' '))
    computer = player.pop(0)
    computerPoint = 0

    for i in range(n):
        getCard = 'Y'

        while (getCard == 'Y'):
            card = input().split(' ')
            getCard = card[0]

            if (getCard == 'Y'):
                player[i] = player[i] + countIndexPoint(card[-1])

            if (player[i] >= 10.5):
                if (player[i] > 10.5):
                    player[i] = 0
                    bet[i] = bet[i] * (-1)
                break

    minPlayer = max(player)

    for i in range(n):
        if (player[i] < minPlayer and player[i] != 0):
            minPlayer = player[i]

    while (computer <= minPlayer and minPlayer < 10.5):
        computer = computer + countIndexPoint(input())

        if (computer >= 10.5):
            if (computer > 10.5):
                computer = -1
            break

    if (computer == -1):
        for i in range(n):
            computerPoint = computerPoint - bet[i]
    else:
        for i in range(n):
            if (player[i] == 10.5):
                computerPoint = computerPoint - bet[i]
            elif (player[i] == 0):
                computerPoint = computerPoint - bet[i]
            elif (computer < player[i]):
                computerPoint = computerPoint - bet[i]
            else:
                computerPoint = computerPoint + bet[i]
                bet[i] = bet[i] * (-1)

    for i in range(n):
        if (bet[i] > 0):
            print("Player%d +" %(i+1), bet[i], sep='')
        else:
            print("Player%d" %(i+1), bet[i])
    
    if (computerPoint > 0):
        print("Computer +%d" %computerPoint)
    else:
        print("Computer %d" %computerPoint)
    
main()