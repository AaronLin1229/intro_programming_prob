prices = [40, 30, 20, 50, 50]
quantities = list(map(int, input().split()))
total_price = sum(q * p for q, p in zip(quantities, prices))
print(total_price)
