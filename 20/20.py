def inputMatrix(row, n):
    matrix = list()

    for i in range(1, n+1):
        matrix.append(i + row * n)

    return matrix

def turnLeft(matrix, n):
    newMatrix = list()

    for i in range(n-1, -1, -1):
        temporary = list()
        for j in range(n):
            temporary.append(matrix[j][i])
        newMatrix.append(temporary)

    return newMatrix

def turnRight(matrix, n):
    newMatrix = list()

    for i in range(n):
        temporary = list()
        for j in range(n-1, -1, -1):
            temporary.append(matrix[j][i])
        newMatrix.append(temporary)

    return newMatrix

def main():
    n, instruction = int(input()), input()

    matrix = list()

    for i in range(n):
        matrix.append(inputMatrix(i, n))

    for i in range(len(instruction)):
        if (instruction[i] == 'L'):
            matrix = turnLeft(matrix, n)
        else:
            matrix = turnRight(matrix, n)

    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()

main()