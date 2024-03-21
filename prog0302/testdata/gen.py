import subprocess
import random
import string

upper = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
lower = [chr(i) for i in range(ord("a"), ord("z") + 1)]
lst = upper + lower

def generate_samples():
    samples = ['A', 'b']
    for i, ch in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(ch)
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(n=30):
    for i in range(1, n + 1):
        ch = random.choice(lst)
        with open(f'{i}.in', 'w') as fin:
            fin.write(ch)
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_samples()
generate_random_cases()
