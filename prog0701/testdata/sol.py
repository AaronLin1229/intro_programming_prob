def check(s):
    if len(s) != 10: return False
    if not s[0].isupper(): return False
    if not s[1: ].isdigit(): return False

    cnt = 0
    letter = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    number = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
    
    for ch, n in zip(letter, number):
        s = s.replace(ch, str(n))

    weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]

    cnt = 0
    for ch, w in zip(s, weight):
        cnt += int(ch) * w

    return cnt % 10 == 0
    

if __name__ == "__main__":
    print("YES" if check(input()) else "NO")