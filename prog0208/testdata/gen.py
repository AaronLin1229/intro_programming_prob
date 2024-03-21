import random
import subprocess

def generate_sample_cases():
    samples = [(2, 4), (1, 4)]
    for i, (h, w) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f"{h}\n{w}\n")
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(n=30):
    for i in range(1, n+1):
        while True:
            a = random.randint(1, 99)
            b = random.randint(1, 99)
            if a < b: break
        with open(f'{i}.in', 'w') as fin:
            fin.write(f"{a}\n{b}\n")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
