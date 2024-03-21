import random
import subprocess

def generate_sample_cases():
    sample = [
        ("2 3\n1 2 3\n4 5 6\n-1 -2 -3\n-4 -5 -6", "0 0 0\n0 0 0"),
        ("3 3\n1 0 -1\n2 0 2\n-1 1 0\n0 1 1\n1 0 -1\n0 -1 0", "1 1 0\n3 0 1\n-1 0 0")
    ]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(data[0])
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)


def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        n, m = random.randint(1, 50), random.randint(1, 50)
        with open(f'{i}.in', 'w') as f:
            f.write(f"{n} {m}\n")
            for _ in range(2 * n):
                f.write(' '.join(str(random.randint(-10, 10)) for _ in range(m)) + '\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
