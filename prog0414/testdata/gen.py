import random
import subprocess

def generate_sample_cases():
    sample_cases = [
        ([1, 2, 3], 6),
        ([-1, 5, 10], 14)
    ]
    for i, (inputs, output) in enumerate(sample_cases, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write('\n'.join(map(str, inputs)))
        with open(f'sample{i}.out', 'w') as f:
            f.write(str(output))

def generate_random_cases(n=30):
    for i in range(1, n + 1):
        case_length = random.randint(1, 100)
        with open(f'{i}.in', 'w') as f:
            f.writelines(f"{random.randint(-10**6, 10**6)}\n" for _ in range(case_length))
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
