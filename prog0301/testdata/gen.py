import subprocess
import random

def generate_sample_cases():
    with open('sample1.in', 'w') as f:
        f.write('4\n')
    subprocess.run('python3 sol.py < sample1.in > sample1.out', shell=True)

    with open('sample2.in', 'w') as f:
        f.write('5\n')
    subprocess.run('python3 sol.py < sample2.in > sample2.out', shell=True)

def generate_random_cases(n=30):
    for i in range(1, n+1):
        with open(f'{i}.in', 'w') as f:
            f.write(f'{random.randint(1, 10**6)}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
