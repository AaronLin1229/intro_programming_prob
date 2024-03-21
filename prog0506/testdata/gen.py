import random
import subprocess

def generate_sample_testcases():
    sample_inputs = [
        [2, 3, 8, 6, 1],  # Sample 1 input
        [4, 3, 2, 1]   # Sample 2 input
    ]
    for i, input_data in enumerate(sample_inputs, start=1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(f'{len(input_data)}\n')
            f.write(' '.join(map(str, input_data)) + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 1e3)
        input_data = [random.randint(1, 1e9) for _ in range(n)]
        with open(f'{i}.in', 'w') as f:
            f.write(f'{n}\n')
            f.write(' '.join(map(str, input_data)) + '\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Generate sample and random test cases
generate_sample_testcases()
generate_random_testcases()
