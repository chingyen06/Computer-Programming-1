def countPoint(card):
    point = ['J', 'Q', 'K']

    if (card in point):
        return 0.5
    
    if (card == 'A'):
        return 1
    
    return int(card)

def computerRule(player, computer):
    if (player > computer or computer <= 8):
        return 1
    
    return 0

def main():
    player, computer = countPoint(input()), countPoint(input())
    getCard = 'Y'
    computerGet = 1

    while(getCard == 'Y' or (computerRule(player, computer) and computerGet == 1)):
        if (getCard == 'Y'):
            getCard = input()
        
        if (getCard == 'Y'):
            player = player + countPoint(input())

        if (player > 10.5):
            player = 0
            break

        if (computerRule(player, computer)):
            if (computerGet == 1):
                computer = computer + countPoint(input())
        else:
            computerGet = 0

        if (computer > 10.5):
            computer = 0
            break

    if (computer > player):
        print("computer win")
    elif (player > computer):
        print("player win")
    else:
        print("it\'s a tie")

main()