import subprocess
import random

def generate_sample_cases():
    samples = ["123", "49"]
    for i, sample in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(sample + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(n=30):
    for i in range(1, n + 1):
        num = random.randint(1, 10**9)
        with open(f'{i}.in', 'w') as fin:
            fin.write(f'{num}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Generate cases
generate_sample_cases()
generate_random_cases()
