import random
import subprocess

def generate_sample_cases():
    sample = [(3, [1, 2, 3]), (3, [3, 2, 1]), (3, [1, 1, 1])]
    for i, (n, a) in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(f"{n}\n{' '.join(map(str, a))}\n")
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        is_sorted = random.choice([True, False])

        n = random.randint(1, 100000)
        a = [random.randint(-100, 100) for _ in range(n)]
        if is_sorted: a.sort()

        with open(f'{i}.in', 'w') as f:
            f.write(f"{n}\n{' '.join(map(str, a))}\n")

        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
