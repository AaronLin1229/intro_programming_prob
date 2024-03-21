h, w = map(int, input().split())
for i in range(h):
    for j in range(w):
        if (i in [0, h-1]) and (j in [0, w-1]):
            print('O', end='')
        elif i in [0, h-1]:
            print('-', end='')
        elif j in [0, w-1]:
            print('|', end='')
        else:
            print(' ', end='')
    print()
