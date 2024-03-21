import random
import subprocess

def generate_sample_testcases():
    samples = [(4, 6), (21, 6)]
    for i, (a, b) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f'{a} {b}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(n=30):
    for i in range(1, n + 1):
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)
        with open(f'{i}.in', 'w') as fin:
            fin.write(f'{a} {b}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Uncomment to generate test cases
generate_sample_testcases()
generate_random_testcases()
