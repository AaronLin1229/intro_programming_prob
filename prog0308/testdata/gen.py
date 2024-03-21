import subprocess
import random

def generate_sample_testcases():
    sample_inputs = [8, 15, 25]
    for i, input_val in enumerate(sample_inputs, 1):
        with open(f'sample{i}.in', 'w') as infile, open(f'sample{i}.out', 'w') as outfile:
            infile.write(f"{input_val}\n")
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(n=30):
    for i in range(1, n + 1):
        with open(f'{i}.in', 'w') as infile:
            if random.choice([True, True, True, True, False]):
                rand_num = random.randint(0, 40)
            else:
                rand_num = random.randint(41, 100)
            infile.write(f"{rand_num}\n")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

# Uncomment the function calls to generate test cases
generate_sample_testcases()
generate_random_testcases()
