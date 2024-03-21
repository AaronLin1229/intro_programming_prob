import subprocess

def generate_samples():
    samples = [
        4, 15
    ]
    for i, inp in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(f"{inp}\n")
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)
        

def generate_random_testcases(n=30):
    for i in range(1, n + 1):
        with open(f'{i}.in', 'w') as f:
            f.write(f"{i * 10}\n")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_samples()
generate_random_testcases()
