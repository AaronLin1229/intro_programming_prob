n = int(input())
arr = list(map(float, input().split()))

mean = sum(arr) / len(arr) 
var = sum((num - mean) ** 2 for num in arr) / len(arr)

print(f"{mean:.15f}")
print(f"{var:.15f}")