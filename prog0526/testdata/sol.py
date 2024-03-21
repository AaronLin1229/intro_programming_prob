row, column = [int(i) for i in input().split()]
columns = []
for _ in range(row):
    columns.append([int(i) for i in input().split()])
max_apple = 0
position= [0, 0]
for i in range(row):
    for j in range(column):
        current_apple = 0
        for k in range(i-1, i+2):
            for l in range(j-1, j+2):
                if k < 0 or l < 0 or k >= row or l >= column:
                    pass
                else:
                    current_apple += columns[k][l]
        if current_apple > max_apple:
            max_apple = current_apple
            position = [i, j]
print(max_apple)
print(*position)