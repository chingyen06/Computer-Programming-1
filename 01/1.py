name = input()
ID = input()
chinese = int(input())
cs101 = int(input())
program = int(input())

print("Name:", name, sep='')
print("ID:", ID, sep='')
print("Average:", (chinese + cs101 + program) // 3, sep='')
print("Total:", chinese + cs101 + program, sep='')
