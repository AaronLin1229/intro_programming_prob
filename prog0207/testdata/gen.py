import random
import subprocess

def generate_samples():
    samples = [32, 212]  # Example test cases
    for i, sample in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f'{sample}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(num=30):
    for i in range(1, num + 1):
        F = random.uniform(-1000, 1000)
        with open(f'{i}.in', 'w') as fin:
            fin.write(f'{F}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_samples()
generate_random_testcases()
