import sys

sum = 0
for line in sys.stdin:
    if line.strip() == '':
        break
    sum += int(line)

print(sum)
