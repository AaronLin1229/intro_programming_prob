import subprocess
import random

def generate_sample_cases():
    samples = [(3, 3), (4, 5)]
    for i, (inp, out) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f'{inp}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)
        

def generate_random_cases(n=30):
    for i in range(1, n + 1):
        with open(f'{i}.in', 'w') as fin:
            fin.write(f'{random.randint(1, 40)}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
