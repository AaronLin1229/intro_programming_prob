import subprocess
import random

def generate_sample_testcases():
    samples = [
        (5, [1, 3, 6, 10, 15]),
        (3, [100, 200, 300])
    ]

    for i, (n, A) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as f_in, open(f'sample{i}.out', 'w') as f_out:
            f_in.write(f'{n}\n')
            f_in.write(' '.join(map(str, A)) + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(num_testcases=30):
    for i in range(1, num_testcases + 1):
        n = random.randint(2, int(1e3))
        A = sorted(random.randint(1, int(1e8)) for _ in range(n))

        with open(f'{i}.in', 'w') as f_in, open(f'{i}.out', 'w') as f_out:
            f_in.write(f'{n}\n')
            f_in.write(' '.join(map(str, A)) + '\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Generate sample testcases
generate_sample_testcases()

# Generate random testcases
generate_random_testcases()
