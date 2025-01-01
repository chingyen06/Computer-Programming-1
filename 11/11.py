import math

def countPrice(discount):
    for i in range(1, 4):
        if (10 * i < discount[0] <= 10 * (i+1)):
            return discount[0] * discount[5] * (discount[i] / 100)
    return discount[0] * discount[5]
    
def main():
    a = list(map(int, input().split(','))) + [100, 380]
    b = list(map(int, input().split(','))) + [100, 1200]
    c = list(map(int, input().split(','))) + [100, 180]

    price = [[math.ceil(countPrice(a)), 'A'], [math.ceil(countPrice(b)), 'B'], [math.ceil(countPrice(c)), 'C']]
    t = 0

    price = sorted(price)

    for i in range(2, -1, -1):
        print(str(price[i][1]) + "," + str(price[i][0]))
        t = t + price[i][0]

    print(t)

if __name__ == "__main__":
    main()
