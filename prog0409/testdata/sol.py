n = int(input())
counts = [0, 0, 0]
for _ in range(n):
    x = int(input())
    counts[x % 3] += 1
print(counts[0], counts[1], counts[2])
