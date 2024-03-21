import random
import subprocess

def generate_sample_testcases():
    samples = [(12, 15), (101, 10)]
    for i, (a, b) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f'{a} {b}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(n=30):
    for i in range(1, n + 1):
        if random.choice([True, False, False]):
            base = 1
        else:
            base = random.randint(1, 10**4)
        b_a = random.randint(1, 10**4)
        b_b = random.randint(1, 10**4)

        a = base * b_a
        b = base * b_b

        with open(f'{i}.in', 'w') as fin:
            fin.write(f'{a} {b}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Uncomment to generate test cases
generate_sample_testcases()
generate_random_testcases()
