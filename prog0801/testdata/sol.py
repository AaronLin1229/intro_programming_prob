import sys

for line in sys.stdin:
    N = int(line)
    print(bin(N).count('1'))
