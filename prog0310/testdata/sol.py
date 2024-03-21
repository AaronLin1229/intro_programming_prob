w, a, b, c, d, e = map(int, input().split())

# Calculation
if b != 0:
    ans = w**2 + (a + b + c + 2 * d + 2 * e + 2)**2
else:
    m = max(d, e)
    ans = w**2 + (a + c + 2 * m + 2)**2

# Output
print(ans)
