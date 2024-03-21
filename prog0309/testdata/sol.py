p = int(input())
currencies = [1000, 500, 100, 50, 10, 5, 1]
count = 0
for c in currencies:
    count += p // c
    p %= c
print(count)
