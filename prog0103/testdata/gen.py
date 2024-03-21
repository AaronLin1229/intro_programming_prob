import subprocess

def generate_samples():
    with open('sample1.in', 'w') as file:
        pass  # No input for this problem
    with open('sample1.out', 'w') as file:
        file.write('Hello, world!\n')

def generate_random_testcases(num_cases=30):
    for i in range(1, num_cases + 1):
        with open(f'{i}.in', 'w') as file:
            pass  # No input for this problem
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_samples()
generate_random_testcases()
