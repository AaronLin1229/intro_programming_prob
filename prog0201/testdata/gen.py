import random
import subprocess

def generate_sample_test_cases():
    sample_inputs = [(3, 5), (7, 9)]
    for i, (a, b) in enumerate(sample_inputs, 1):
        with open(f'sample{i}.in', 'w') as infile:
            infile.write(f"{a}\n{b}\n")
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_test_cases(n=30):
    for i in range(1, n + 1):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        with open(f'{i}.in', 'w') as infile:
            infile.write(f"{a}\n{b}\n")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_test_cases()
generate_random_test_cases()
