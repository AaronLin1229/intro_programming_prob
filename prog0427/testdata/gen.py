import random
import subprocess

def generate_sample_testcases():
    sample_inputs = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [5, 5, 5, 4, 3, 4, 5, 5, 5]
    ]
    for i, (lst) in enumerate(sample_inputs, start = 1):
        with open(f'sample{i}.in', 'w') as infile:
            lst = list(map(str, lst))
            infile.write("\n".join(lst))
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_testcases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 2e5)
        with open(f'{i}.in', 'w') as infile:
            for _ in range(n):
                this_num = random.randint(1, 1e2)
                infile.write(f'{this_num}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)


generate_sample_testcases()
generate_random_testcases()
