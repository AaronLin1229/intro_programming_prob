def collatz_sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    print(1)

collatz_sequence(int(input()))