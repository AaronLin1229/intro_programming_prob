import random
import subprocess

def generate_sample_cases():
    sample = [(3, 5), (-2, 4)]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(f'{data[0]} {data[1]}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        a = random.randint(-10**9, 10**9)
        b = random.randint(-10**9, 10**9)
        with open(f'{i}.in', 'w') as f:
            f.write(f'{a} {b}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
