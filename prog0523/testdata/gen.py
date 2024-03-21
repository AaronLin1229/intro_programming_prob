import random
import subprocess

def generate_sample_cases():
    sample = [
        "3 3\n1 2 3\n4 5 6\n7 8 9\n", 
        "4 3\n1 2 3\n4 5 6\n7 8 9\n10 11 12\n"
    ]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(data)
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 1000)
        m = random.randint(1, 1000)
        with open(f'{i}.in', 'w') as f:
            f.write(f'{n} {m}\n')
            for _ in range(n):
                f.write(' '.join(str(random.randint(1, 1000)) for _ in range(m)) + '\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
