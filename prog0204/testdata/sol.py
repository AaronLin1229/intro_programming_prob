s, f, t = map(int, input().split())

c = s - t
b = (f // 2) - (4 * c) - t
a = t - b

print(a, b, c, sep = '\n')