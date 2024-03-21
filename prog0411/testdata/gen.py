import subprocess

def generate_sample_test_cases():
    samples = [13, 5]

    for i, (inp) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(f'{inp}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_test_cases():
    from random import randint

    for i in range(1, 31):
        if i == 1: n = 1
        elif i == 2: n = 113383
        else: n = randint(1, 10**6)
        with open(f'{i}.in', 'w') as f:
            f.write(f'{n}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Uncomment the function call to generate test cases
generate_sample_test_cases()
generate_random_test_cases()

# 1
# 113383