def isPrime(dna):
    l = len(dna)
    count = 0

    for i in range(1, l+1):
        if (l % i == 0):
            count += 1

    if (count == 2):
        return 1
    
    return 0

def main():
    first = input()
    last = input().split()
    dna = input()
    ans = list()

    for i in range(len(dna)-len(first)+1):
        a = i + len(first)

        if (dna[i:a] == first):
            for j in range(a, len(dna)-len(last[0])+1):
                if (dna[j:j+len(last[0])] in last):
                    if (isPrime(dna[a:j])):
                        ans.append([len(dna[a:j]), dna[a:j]])
                    break
    
    ans = sorted(ans)

    for i in ans:
        print(i[1])
    
    if (len(ans) == 0):
        print("No gene")

main()