import random
import subprocess

def generate_sample_cases():
    samples = [(5, 1, [3]), (6, 2, [2, 4])]
    for i, (N, K, broken) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f'{N}\n{K}\n')
            fin.write(' '.join(map(str, broken)) + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(n=30):
    for i in range(1, n + 1):
        can_be_zero = random.choice([True, False])

        while True:
            N = random.randint(1, 40)
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
                fin.write(f'{N}\n{K}\n')
                fin.write(' '.join(map(str, broken)) + '\n')

            subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

            if can_be_zero == True:
                break
            else:
                with open(f'{i}.out', 'r') as f:
                    number = int(f.readline().strip())
                    if number != 0:
                        break

generate_sample_cases()
generate_random_cases()
