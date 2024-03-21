import random
import subprocess

def generate_sample_test_cases():
    samples = [(3, 4, 5), (1, 2, 3)]
    for i, (a, b, c) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f"{a} {b} {c}")
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_test_cases(n=30):
    for i in range(1, n + 1):
        a, b, c = random.randint(1, 10**6), random.randint(1, 10**6), random.randint(1, 10**6)
        with open(f'{i}.in', 'w') as fin:
            fin.write(f"{a} {b} {c}")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_test_cases()
generate_random_test_cases()
