import random
import subprocess

def generate_sample_cases():
    samples = [
        ((1, 2), (3, 4)),
        ((0, 2), (3, 1))
    ]
    for i, ((a, b), (c, d)) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(f'{a} {b}\n{c} {d}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        a, b, c, d = [random.randint(-100, 100) for _ in range(4)]
        with open(f'{i}.in', 'w') as f:
            f.write(f'{a} {b}\n{c} {d}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
