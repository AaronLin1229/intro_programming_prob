import subprocess
import random

def generate_sample_testcases():
    samples = ["15", "21"]
    for i, sample in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as f_in, open(f'sample{i}.out', 'w') as f_out:
            f_in.write(sample + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(num=30):
    for i in range(1, num + 1):
        x = random.randint(1, 10**6)
        with open(f'{i}.in', 'w') as f_in:
            f_in.write(f'{x}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_testcases()
generate_random_testcases()
