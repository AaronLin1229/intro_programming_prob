import random
import subprocess

def generate_sample_cases():
    sample = [
        ([2, 3], [[1, 2, 3], [4, 5, 6]]),
        ([3, 2], [[7, 8], [9, 10], [11, 12]])
    ]
    for i, (dims, data) in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(f'{dims[0]} {dims[1]}\n')
            for row in data:
                f.write(' '.join(map(str, row)) + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        if i == 28: n, m = 1, random.randint(1, 1000)
        elif i == 29: n, m = random.randint(1, 1000), 1
        elif i == 30: n, m = 1, 1
        else: n, m = random.randint(1, 1000), random.randint(1, 1000)


        with open(f'{i}.in', 'w') as f:
            f.write(f'{n} {m}\n')
            for _ in range(n):
                f.write(' '.join(str(random.randint(-10**9, 10**9)) for _ in range(m)) + '\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
