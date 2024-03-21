import random
import subprocess

def generate_sample_cases():
    samples = [(1, 2), (100000, 200000)]
    for i, (a, b) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f"{a}\n{b}\n")
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        a = random.randint(0, 1_000_000)
        b = random.randint(0, 1_000_000)
        with open(f'{i}.in', 'w') as fin:
            fin.write(f"{a}\n{b}\n")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Generate sample and random test cases
generate_sample_cases()
generate_random_cases()
