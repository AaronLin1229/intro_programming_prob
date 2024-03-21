import random
import subprocess

def generate_sample_cases():
    samples = [(4, 2), (5, 3)]
    for i, (N, M) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f'{N}\n{M}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(n=30):
    for i in range(1, n + 1):
        while True:
            N = random.randint(1, 40)
            M = min([random.randint(1, N) for i in range(2)])
            with open(f'{i}.in', 'w') as fin:
                fin.write(f'{N}\n{M}\n')
            subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

            with open(f"{i}.out", 'r') as f:
                number = int(f.readline().strip())
                if number < 2147483647: break

generate_sample_cases()
generate_random_cases()
