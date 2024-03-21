import random
import subprocess

def generate_sample_cases():
    samples = [(5, 2, 1, [3]), (6, 3, 2, [2, 5])]
    for i, (N, M, K, broken) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f'{N}\n{M}\n{K}\n')
            fin.write(' '.join(map(str, broken)) + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(n=30):
    for i in range(1, n + 1):
        while True:
            can_be_zero = random.choice([True, False])

            N = random.randint(1, 40)
            M = min([random.randint(1, N) for i in range(2)])
            if N == 1:
                K = random.randint(1, 1)
            elif N == 2:
                K = random.randint(1, 2)
            else:
                p_pool = [[i] * (N - i + 1) for i in range(1, (N + 1) // 2)]
                pool = []
                for lst in p_pool: pool += lst
                K = random.choice(pool)
            broken = sorted(random.sample(range(1, N + 1), K))

            with open(f'{i}.in', 'w') as fin:
                fin.write(f'{N}\n{M}\n{K}\n')
                fin.write(' '.join(map(str, broken)) + '\n')

            subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

            with open(f"{i}.out", 'r') as f:
                number = int(f.readline().strip())
                if number > 2147483647: continue
            
            with open(f'{i}.out', 'r') as f:
                number = int(f.readline().strip())
                if number == 0 and can_be_zero == False: continue

            break

generate_sample_cases()
generate_random_cases()
