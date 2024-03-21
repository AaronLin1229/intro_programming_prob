import random
import subprocess

def generate_sample_testcases():
    samples = [(5, [1, 4, 8, 9, 10]), (5, [10, 20, 30, 40, 50])]
    for i, (n, arr) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f'{n}\n')
            fin.write(' '.join(map(str, arr)) + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 1000)
        arr = [random.randint(1, 1000) for _ in range(n)]
        with open(f'{i}.in', 'w') as fin:
            fin.write(f'{n}\n')
            fin.write(' '.join(map(str, arr)) + '\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_testcases()
generate_random_testcases()
