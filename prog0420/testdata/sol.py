h, w = map(int, input().split())
for i in range(h):
    line = ""
    for j in range(w):
        if (i + j) % 2 == 0:
            line += "+"
        else:
            line += "-"
    print(line)
