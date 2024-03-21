import random
import subprocess

def generate_sample_cases():
    sample_inputs = ['3\n', '5\n']
    sample_outputs = ['3\n2\n1\n', '5\n4\n3\n2\n1\n']
    for i, (inp, out) in enumerate(zip(sample_inputs, sample_outputs), 1):
        with open(f'sample{i}.in', 'w') as f_in, open(f'sample{i}.out', 'w') as f_out:
            f_in.write(inp)
            f_out.write(out)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        with open(f'{i}.in', 'w') as f_in:
            n = random.randint(1, 10**3)
            f_in.write(f'{n}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
