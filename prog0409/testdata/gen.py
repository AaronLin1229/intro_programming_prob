import random
import subprocess

def generate_samples():
    samples = [
        (5, [1, 2, 3, 4, 5]),
        (10, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    ]
    for i, (n, nums) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(f'{n}\n')
            for num in nums:
                fin.write(f'{num}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 20)  # Adjusted according to the specification
        nums = [random.randint(0, 10**9) for _ in range(n)]
        with open(f'{i}.in', 'w') as fin:
            fin.write(f'{n}\n')
            for num in nums:
                fin.write(f'{num}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_samples()
generate_random_testcases()
