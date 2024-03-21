import random
import subprocess

def generate_sample_cases():
    samples = [(1, 1, 1, 1, 1), (0, 2, 5, 1, 3)]
    for i, quantities in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(' '.join(map(str, quantities)) + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        quantities = [random.randint(0, 25) for _ in range(5)]
        with open(f'{i}.in', 'w') as fin:
            fin.write(' '.join(map(str, quantities)) + '\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Generate sample and random test cases
generate_sample_cases()
generate_random_cases()
