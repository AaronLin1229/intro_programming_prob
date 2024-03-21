import random
import subprocess

def generate_sample_cases():
    samples = [(3, 5), (2, 2)]
    for i, (h, w) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f"{h} {w}\n")
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(n=30):
    for i in range(1, n+1):
        h = random.randint(1, 10)
        w = random.randint(1, 10)
        with open(f'{i}.in', 'w') as fin:
            fin.write(f"{h} {w}\n")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
