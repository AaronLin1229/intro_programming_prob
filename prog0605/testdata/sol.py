def C(n, k):
    result = 1
    k = min(k, n - k)
    for i in range(k):
        result *= n - i
        result //= i + 1
    return result

n, k = map(int, input().split())
print(C(n, k))
