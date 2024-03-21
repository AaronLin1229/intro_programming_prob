import math

a, b, c = map(int, input().split())
d = b**2 - 4*a*c

if d < 0:
    print(0)
elif d == 0:
    print(1)
    print("{:.15f}".format(-b / (2.0 * a)))
else:
    print(2)
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print("{:.15f} {:.15f}".format(min(x1, x2), max(x1, x2)))
