import random
import subprocess

def generate_sample_cases():
    sample = [
        ([2, 3, 2], [[1, 0, 2], [-1, 3, 1]], [[3, 1], [2, 1], [1, 0]]),
        ([3, 2, 3], [[1, 2], [3, 4], [5, 6]], [[1, 1, 1], [2, 2, 2]])
    ]
    for i, (dims, matrix_a, matrix_b) in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(f"{dims[0]} {dims[1]} {dims[2]}\n")
            for row in matrix_a:
                f.write(' '.join(map(str, row)) + '\n')
            for row in matrix_b:
                f.write(' '.join(map(str, row)) + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        if i == 30: n, m, k = 1, 1, 1
        elif i == 29: n, m, k = random.randint(1, 50), 1, random.randint(1, 50)
        elif i == 28: n, m, k = 1, random.randint(1, 50), 1
        else: n, m, k = random.randint(1, 50), random.randint(1, 50), random.randint(1, 50)

        matrix_a = [[random.randint(-10, 10) for _ in range(m)] for _ in range(n)]
        matrix_b = [[random.randint(-10, 10) for _ in range(k)] for _ in range(m)]
        with open(f'{i}.in', 'w') as f:
            f.write(f"{n} {m} {k}\n")
            for row in matrix_a:
                f.write(' '.join(map(str, row)) + '\n')
            for row in matrix_b:
                f.write(' '.join(map(str, row)) + '\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()  
