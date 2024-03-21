import random
import subprocess

def generate_sample_cases():
    sample = [('4 4\n*...\n....\n.*..\n....\n', '*100\n2210\n1*10\n1110\n')]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(data[0])
        with open(f'sample{i}.out', 'w') as f:
            f.write(data[1])
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        n, m = random.randint(1, 100), random.randint(1, 100)
        with open(f'{i}.in', 'w') as f:
            f.write(f'{n} {m}\n')
            for _ in range(n):
                row = ''.join(random.choice(['.', '.', '*']) for _ in range(m))
                f.write(row + '\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
