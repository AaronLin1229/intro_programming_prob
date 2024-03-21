import random
import subprocess

def generate_sample_cases():
    sample = [
        ([1, 1, 2, 2, 3], "sample1"),
        ([2, 2, 2, 2], "sample2")
    ]
    for i, (data, filename) in enumerate(sample, 1):
        with open(f'{filename}.in', 'w') as file:
            file.write(f"{len(data)}\n")
            file.write(' '.join(map(str, data)))
        subprocess.run(f'python3 sol.py < {filename}.in > {filename}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        if i == 30:
            n = 1000
            data = [i for i in range(1, n + 1)]
        else:
            n = random.randint(1, 1000)
            data = sorted([random.randint(0, 1000) for _ in range(n)])

        with open(f'{i}.in', 'w') as file:
            file.write(f"{n}\n")
            file.write(' '.join(map(str, data)))
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
