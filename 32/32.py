def areaCheck(sudoku, n, fill):
    if (n // 4 % 2 != 0):
        n = n - 4
    
    if (n % 4 % 2 != 0):
        n = n - 1
    
    if (sudoku[n] == fill or sudoku[n+1] == fill or sudoku[n+4] == fill or sudoku[n+5] == fill):
        return 0
    
    return 1

def check(sudoku, n, fill):
    for i in range(n-n%4, n-n%4+4):
        if (sudoku[i] == fill):
            return 0
        
    for i in range(n-n//4*4, n-n//4*4+13, 4):
        if (sudoku[i] == fill):
            return 0
        
    return areaCheck(sudoku, n, fill)

def dfs(sudoku, n):
    for i in range(n, 16):
        if (sudoku[i] == 0):
            ok = 0
            for j in range(1, 5):
                if (check(sudoku, i, j) and sudoku[i] == 0):
                    ok = 1
                    sudoku[i] = j
                    if (dfs(sudoku, i + 1)[1] == 0):
                        sudoku[i] = 0
            if (ok == 0):
                return sudoku, 0
            
    if (0 not in sudoku):
        return sudoku, 1
        

def main():
    sudoku = list()

    for i in range(4):
        temp = list(map(int, input().split()))

        sudoku.extend(temp)

    sudoku, a = dfs(sudoku, 0)

    for i in range(4):
        for j in range(4):
            print(sudoku[i*4+j], end=' ')
        print()

main()