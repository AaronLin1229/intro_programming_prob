import random
import subprocess

def generate_sample_testcases():
    samples = [
        (10, 30, 12, 45),
        (23, 59, 0, 1)
    ]
    for i, (h1, m1, h2, m2) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f"{h1} {m1}\n{h2} {m2}\n")
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(n=30):
    for i in range(1, n + 1):
        h1, m1 = random.randint(0, 23), random.randint(0, 59)
        h2, m2 = random.randint(0, 23), random.randint(0, 59)
        with open(f'{i}.in', 'w') as fin:
            fin.write(f"{h1} {m1}\n{h2} {m2}\n")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Uncomment to generate testcases
generate_sample_testcases()
generate_random_testcases()
