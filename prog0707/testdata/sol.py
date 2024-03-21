def format_with_commas(n):
    result = ''
    count = 0
    for i in range(len(n) - 1, -1, -1):
        result = n[i] + result
        count += 1
        if count % 3 == 0 and i != 0:
            result = ',' + result
    return result

n = input()
print(format_with_commas(n))
