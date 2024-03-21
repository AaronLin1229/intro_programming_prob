

try:
    now_max_num = -1
    now_cnt = 0
    while True:
        x = int(input())
        if x > now_max_num:
            now_max_num = x
            now_cnt = 1
        elif x == now_max_num:
            now_cnt += 1

        print(f"{now_max_num} {now_cnt}")

except EOFError:
    pass