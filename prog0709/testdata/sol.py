N = int(input())
strings = [input() for _ in range(N)]

strings.sort()

for string in strings:
    print(string)
