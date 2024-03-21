import subprocess

def generate_sample_test_cases():
    samples = ["3", "5"]
    for i, sample in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(sample)
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_test_cases(n=30):
    from random import randint
    for i in range(1, n+1):
        with open(f'{i}.in', 'w') as f:
            f.write(f"{randint(1, 100)}\n")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Uncomment the function you want to run
generate_sample_test_cases()
generate_random_test_cases()
