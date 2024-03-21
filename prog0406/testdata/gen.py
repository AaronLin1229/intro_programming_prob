import subprocess

def generate_samples():
    samples = [
        (3, 'sample1'),
        (5, 'sample2')
    ]
    for x, fname in samples:
        with open(f'{fname}.in', 'w') as fin:
            fin.write(f'{x}\n')
        subprocess.run(f'python3 sol.py < {fname}.in > {fname}.out', shell=True)

def generate_random_testcases():
    import random
    for i in range(1, 31):
        x = 15 + i
        with open(f'{i}.in', 'w') as fin:
            fin.write(f'{x}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Call the functions to generate the test data
generate_samples()
generate_random_testcases()
