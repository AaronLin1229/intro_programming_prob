import subprocess
import random

def generate_samples():
    samples = [
        (5, [1, 3, 5, 5, 2]),
        (3, [10, 10, 10])
    ]

    for i, (n, A) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f'{n}\n')
            fin.write(' '.join(map(str, A)) + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(num_testcases=30):
    for i in range(1, num_testcases + 1):
        n = random.randint(1, 10**5)
        A = [random.randint(-10**4, 10**4) for _ in range(n)]

        with open(f'{i}.in', 'w') as fin:
            fin.write(f'{n}\n')
            fin.write(' '.join(map(str, A)) + '\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_samples()
generate_random_testcases()
       
