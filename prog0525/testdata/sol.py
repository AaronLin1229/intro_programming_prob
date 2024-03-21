n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]
C = [[sum(A[i][r] * B[r][j] for r in range(m)) for j in range(k)] for i in range(n)]

for row in C:
    print(*row)
