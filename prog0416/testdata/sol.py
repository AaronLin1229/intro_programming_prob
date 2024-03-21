n = input().strip()
sumOdd = sum(int(n[i]) for i in range(len(n)) if i % 2 != 0)
sumEven = sum(int(n[i]) for i in range(len(n)) if i % 2 == 0)

if abs(sumOdd - sumEven) % 11 == 0:
    print("YES")
else:
    print("NO")
