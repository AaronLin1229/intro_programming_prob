import random
import subprocess

def generate_sample_cases():
    sample = [(5, 2), (6, 3)]
    for i, (n, k) in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as file:
            file.write(f'{n} {k}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(0, 12)
        k = random.randint(0, n)
        with open(f'{i}.in', 'w') as file:
            file.write(f'{n} {k}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()