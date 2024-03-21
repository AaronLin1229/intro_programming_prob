n = int(input())
lst = list(map(int, input().split()))

for i in range(n):
    found = False
    for j in range(n):
        if i != j and lst[i] == lst[j]:
            found = True
            break
    if found: continue
    else:
        print(lst[i])
        break
