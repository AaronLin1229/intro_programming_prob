import random
import subprocess

def generate_samples():
    samples = [
        (3, 5),
        (7, 7)
    ]
    for i, (a, b) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(f'{a} {b}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(n=30):
    for i in range(1, n+1):
        a = random.randint(1, 10**9)
        b = random.randint(1, 10**9)
        with open(f'{i}.in', 'w') as f:
            f.write(f'{a} {b}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

if __name__ == "__main__":
    generate_samples()
    generate_random_testcases()
