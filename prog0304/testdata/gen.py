import subprocess

def generate_sample_test_cases():
    samples = [2000, 1900, 2038, 2024]
    for i, sample in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(f"{sample}\n")
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_test_cases():
    import random
    for i in range(1, 31):
        year = random.randint(1, 10**6)
        with open(f'{i}.in', 'w') as f:
            f.write(f"{year}\n")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Uncomment the function you want to use
generate_sample_test_cases()
generate_random_test_cases()
