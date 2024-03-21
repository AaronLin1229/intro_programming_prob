def gcd(a, b):
    while b != 0:
        t = a % b
        a = b
        b = t
    return a

a, b = map(int, input().split())
g = gcd(a, b)
print(a * b // g)