import random
import subprocess

def generate_sample_testcases():
    samples = [
        ([1, 2, 3], [4, 5, 6]),
        ([-1, 0, 3], [4, 5, -2])
    ]
    for i, (v1, v2) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(' '.join(map(str, v1)) + '\n')
            fin.write(' '.join(map(str, v2)))
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(n=30):
    for i in range(1, n+1):
        v1 = [random.randint(-100, 100) for _ in range(3)]
        v2 = [random.randint(-100, 100) for _ in range(3)]
        with open(f'{i}.in', 'w') as fin:
            fin.write(' '.join(map(str, v1)) + '\n')
            fin.write(' '.join(map(str, v2)))
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_testcases()
generate_random_testcases()
