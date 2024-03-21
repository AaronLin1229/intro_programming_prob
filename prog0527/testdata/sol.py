r, c = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    for j in range(c):
        isGreater = True
        if i > 0 and A[i][j] <= A[i-1][j]:
            isGreater = False
        if i < r-1 and A[i][j] <= A[i+1][j]:
            isGreater = False
        if j > 0 and A[i][j] <= A[i][j-1]:
            isGreater = False
        if j < c-1 and A[i][j] <= A[i][j+1]:
            isGreater = False
        if isGreater:
            print(A[i][j])
