import random
import subprocess

def generate_sample_cases():
    sample = [
        (3, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
        (2, 2, [[10, 20], [30, 40]])
    ]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            n, m, matrix = data
            f.write(f"{n} {m}\n")
            for row in matrix:
                f.write(' '.join(map(str, row)) + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        with open(f'{i}.in', 'w') as f:
            if i != 30: n, m = random.randint(1, 1000), random.randint(1, 1000)
            elif i == 30: n, m = 1, 1
            
            f.write(f"{n} {m}\n")
            for _ in range(n):
                row = [random.randint(-1e6, 1e6) for _ in range(m)]
                f.write(' '.join(map(str, row)) + '\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
