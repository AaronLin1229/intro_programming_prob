import random
import subprocess

def generate_sample_cases():
    sample = [
        [5, 3, 2, 4, 1],
        [10, 7, 8, 9]
    ]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as file:
            file.write(f"{len(data)}\n")
            file.write(' '.join(map(str, data)) + "\n")
        with open(f'sample{i}.out', 'w') as file:
            file.write(' '.join(map(str, sorted(data))) + "\n")

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 1000)
        data = [random.randint(-1000, 1000) for _ in range(n)]
        with open(f'{i}.in', 'w') as file:
            file.write(f"{len(data)}\n")
            file.write(' '.join(map(str, data)) + "\n")
        with open(f'{i}.out', 'w') as file:
            file.write(' '.join(map(str, sorted(data))) + "\n")

generate_sample_cases()
generate_random_cases()
