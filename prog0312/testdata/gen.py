import subprocess
import random

def generate_sample():
    with open('sample1.in', 'w') as f:
        f.write("1 -3 2\n")
    with open('sample2.in', 'w') as f:
        f.write("1 4 4\n")
    # subprocess.run('python3 sol.py < sample1.in > sample1.out', shell=True)
    # subprocess.run('python3 sol.py < sample2.in > sample2.out', shell=True)

def generate_random_testcases(n=30):
    for i in range(1, n+1):
        with open(f'{i}.in', 'w') as f:
            a = random.randint(1, 10**3)
            b = random.randint(1, 10**3)
            c = random.randint(1, 10**3)
            f.write(f"{a} {b} {c}\n")
        # subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample()
generate_random_testcases()
