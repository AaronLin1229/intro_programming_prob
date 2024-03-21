

def is_upper(ch):
    return ord('A') <= ord(ch) <= ord('Z')

def is_lower(ch):
    return ord('a') <= ord(ch) <= ord('z')

def solve(s, k):
    ans = ''
    for ch in s:
        if is_upper(ch):
            n = ord(ch) - ord('A')
            n += k + (1000 * 26)
            n %= 26
            ans += chr(n + ord('A')) 
        elif is_lower(ch):
            n = ord(ch) - ord('a')
            n += k + (1000 * 26)
            n %= 26
            ans += chr(n + ord('a')) 
        else:
            ans += ch
    return ans



k = int(input())
try:
    while True:
        print(solve(input(), k))
except EOFError:
    pass