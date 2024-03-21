import random
import subprocess

def generate_sample_cases():
    sample = [
        ([1, 3, 5], [2, 4, 6, 8]),
        ([1, 2], [3, 4, 5])
    ]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(f"{len(data[0])}\n")
            f.write(' '.join(map(str, data[0])) + "\n")
            f.write(f"{len(data[1])}\n")
            f.write(' '.join(map(str, data[1])) + "\n")
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        size_a = random.randint(1, i * 1000)
        size_b = random.randint(1, i * 1000)
        A = sorted(random.randint(0, 10000) for _ in range(size_a))
        B = sorted(random.randint(0, 10000) for _ in range(size_b))
        with open(f'{i}.in', 'w') as f:
            f.write(f"{size_a}\n")
            f.write(' '.join(map(str, A)) + "\n")
            f.write(f"{size_b}\n")
            f.write(' '.join(map(str, B)) + "\n")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
