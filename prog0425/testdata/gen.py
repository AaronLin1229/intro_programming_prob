import random
import subprocess

def generate_sample_testcases():
    sample_inputs = [
        ("1234", "1253"),
        ("5678", "5768")
    ]
    for i, (num1, num2) in enumerate(sample_inputs, start = 1):
        with open(f'sample{i}.in', 'w') as infile:
            infile.write(f'{num1} {num2}\n')
        subprocess.run(f'./out < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(num_cases=30):
    for i in range(1, num_cases + 1):
        num1 = ''.join(random.sample('123456789', 4))
        num2 = ''.join(random.sample('123456789', 4))
        with open(f'{i}.in', 'w') as infile:
            infile.write(f'{num1} {num2}\n')
        subprocess.run(f'./out < {i}.in > {i}.out', shell=True)


generate_sample_testcases()
generate_random_testcases()
