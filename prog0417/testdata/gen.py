import subprocess
import random
import string

def generate_sample_testcases():
    samples = [
        (3, ["Hello, World!", "Zebra-123"]),
        (-1, ["abc XYZ"])
    ]
    for i, (shift, texts) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as infile, open(f'sample{i}.out', 'w') as outfile:
            infile.write(f'{shift}\n')
            infile.write('\n'.join(texts))
        subprocess.run(f'./out < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(n=30):
    for i in range(1, n + 1):
        with open(f'{i}.in', 'w') as infile, open(f'{i}.out', 'w') as outfile:
            shift = random.randint(-100, 100)
            lines = random.randint(1, 5)
            infile.write(f'{shift}\n')
            for _ in range(lines):
                line = ''.join(random.choice(string.ascii_letters + string.digits + " ,.!-") for _ in range(random.randint(1, 50)))
                infile.write(line + '\n')
        subprocess.run(f'./out < {i}.in > {i}.out', shell=True)

generate_sample_testcases()
generate_random_testcases()
