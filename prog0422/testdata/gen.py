import subprocess

def generate_sample_testcases():
    samples = ['3', '5']
    for i, sample in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as fin:
            fin.write(sample + '\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(n=30):
    import random
    for i in range(1, n + 1):
        k = random.randint(1, 100)
        with open(f'{i}.in', 'w') as fin:
            fin.write(f'{k}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Uncomment to generate testcases
generate_sample_testcases()
generate_random_testcases()
