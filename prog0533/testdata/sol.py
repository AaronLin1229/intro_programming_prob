def get_adjacent_mines(field, x, y):
    mines = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(field) and 0 <= ny < len(field[0]) and field[nx][ny] == '*':
                mines += 1
    return mines

n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if field[i][j] == '.':
            field[i][j] = str(get_adjacent_mines(field, i, j))

for row in field:
    print(''.join(row))
