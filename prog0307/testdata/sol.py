h1, m1 = map(int, input().split())
h2, m2 = map(int, input().split())


t1 = h1 * 60 + m1
t2 = h2 * 60 + m2
diff = t2 - t1

if diff < 0:
    diff += 24 * 60

h = diff // 60
m = diff % 60

print(h, m)