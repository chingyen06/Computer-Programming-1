def countPoint(card):
    point = ['A', 'J', 'Q', 'K']

    if (card in point):
        return 0.5
    
    return int(card)

def firstRule(player, banker, playerName, bankerName):
    if (player > 10.5):
        print(bankerName + " Win")
        return None
    
    if (banker > 10.5):
        banker = 0
    
    if (banker > player):
        print(bankerName + " Win")
    elif (player > banker):
        print(playerName + " Win")
    else:
        print("Tie")


def secondRule(player, banker, playerName, bankerName):
    if (player > 10.5):
        player = 0
    
    if (banker > 10.5):
        banker = 0
    
    if (banker > player):
        print(bankerName + " Win")
    elif (player > banker):
        print(playerName + " Win")
    else:
        print("Tie")

def main():
    playerName = input()
    player = [countPoint(input()), countPoint(input()), countPoint(input())]
    bankerName = input()
    banker = [countPoint(input()), countPoint(input()), countPoint(input())]

    firstRule(sum(player), sum(banker), playerName, bankerName)
    secondRule(sum(player), sum(banker), playerName, bankerName)

if __name__ == "__main__":
    main()
