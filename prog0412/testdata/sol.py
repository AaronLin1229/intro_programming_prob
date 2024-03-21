def gcd(a, b):
    while b != 0:
        t = a % b
        a = b
        b = t
    return a

a, b = map(int, input().split())
print(gcd(a, b))
