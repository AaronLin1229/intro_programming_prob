import random
import subprocess

def generate_samples():
    samples = ["11111111111111111111", "9000000009000000009"]
    for i, sample in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(sample)
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(num=30):
    for i in range(1, num + 1):
        ver = random.choice([True, False])

        if i == 1:
            n = 0
        else:
            while True:
                n = random.randint(0, 10**1023)
                if (n % 11 == 0) == ver: break
            
        n = str(n)
        with open(f'{i}.in', 'w') as fin:
            fin.write(n)
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_samples()
generate_random_testcases()
