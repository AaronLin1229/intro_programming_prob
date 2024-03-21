import random
import subprocess

def generate_sample_cases():
    sample = [
        ("3 3\n1 2 3\n4 5 6\n7 8 9\n"),
        ("2 3\n7 8 3\n4 5 6\n")
    ]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(data)
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        r, c = random.randint(1, 100), random.randint(1, 100)
        with open(f'{i}.in', 'w') as f:
            f.write(f'{r} {c}\n')
            for _ in range(r):
                f.write(' '.join(str(random.randint(-10**9, 10**9)) for _ in range(c)) + '\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
