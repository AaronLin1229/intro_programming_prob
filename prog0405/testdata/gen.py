import subprocess

def generate_samples():
    samples = [("5", "120"), ("3", "6")]
    for i, (inp, out) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as infile, open(f'sample{i}.out', 'w') as outfile:
            infile.write(inp)
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases():
    from random import randint
    for i in range(1, 21 + 1):
        x = i - 1
        with open(f'{i}.in', 'w') as infile:
            infile.write(f'{x}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_samples()
generate_random_testcases()
