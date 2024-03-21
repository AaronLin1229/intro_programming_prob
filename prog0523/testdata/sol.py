n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

rotated_matrix = list(zip(*matrix[::-1]))
for row in rotated_matrix:
    print(' '.join(map(str, row)))
