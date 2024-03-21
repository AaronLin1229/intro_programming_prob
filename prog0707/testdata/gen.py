import random
import subprocess

def generate_sample_cases():
    sample = [123456789, 1000]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as file:
            file.write(str(data))
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 10**(i * 30 - random.randint(0, 2)))
        with open(f'{i}.in', 'w') as file:
            file.write(str(n))
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
