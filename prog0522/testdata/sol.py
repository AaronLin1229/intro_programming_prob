n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

transposed_matrix = [[matrix[j][i] for j in range(n)] for i in range(m)]

for row in transposed_matrix:
    print(*row)
