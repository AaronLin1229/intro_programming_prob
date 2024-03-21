N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

c = sorted(A + B)
print(*c, sep = ' ')
