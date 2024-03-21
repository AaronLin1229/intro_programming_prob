import random
import subprocess

import random
import subprocess

def generate_sample_cases():
    sample = [[5, [2, 1, 5, 3, 1]], [4, [1, 2, 3, 4]], [8, [3, 1, 4, 1, 5, 9, 2, 6]]]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as file:
            file.write(f'{len(data[1])}\n')
            file.write(' '.join(map(str, data[1])) + '\n')
        subprocess.run(f'./out < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, 13 + 1):
        subprocess.run(f"./out < {i}.in > {i}.out", shell=True)

    for i in range(13, 30 + 1):
        n = random.randint(1, 2e4)
        A = [random.randint(1, 1e4) for _ in range(n)]
        with open(f'{i}.in', 'w') as file:
            file.write(f'{n}\n')
            file.write(' '.join(map(str, A)) + '\n')
        subprocess.run(f'./out < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()



