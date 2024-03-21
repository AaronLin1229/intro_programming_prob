import random
import subprocess

def generate_samples():
    samples = [43, 123456]
    for i, sample in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f'{sample}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(n=30):
    for i in range(1, n+1):
        p = random.randint(1, 10**6)
        with open(f'{i}.in', 'w') as fin:
            fin.write(f'{p}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Generate sample test cases
generate_samples()
# Generate random test cases
generate_random_testcases()
