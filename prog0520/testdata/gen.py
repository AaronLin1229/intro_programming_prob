import random
import subprocess

def generate_sample_cases():
    sample = [
        [1, -3, 2, 1, -1],
        [-1, -2, -3]
    ]
    for i, lst in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(f'{len(lst)}\n')
            f.write(' '.join(map(str, lst)))
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        N = random.randint(1, 3 * 10**3)

        delta = i - 15
        if i == 1:
            A = [random.randint(-1500, -1) for _ in range(N)]
        else:
            A = [random.randint(-1500 + delta * 100, 1500 + delta * 100) for _ in range(N)]

        with open(f'{i}.in', 'w') as f:
            f.write(f'{N}\n')
            f.write(' '.join(map(str, A)))
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
