import random
import subprocess

def generate_sample_cases():
    for i in range(1, 2 + 1):       
       subprocess.run(f'./out < sample{i}.in > sample{i}.out', shell = True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        with open(f'{i}.in', 'w') as f:
            n = random.randrange(1, 99 + 1, 2)
            lst = [i for i in range(1, n * n + 1)]
            random.shuffle(lst)
            f.write(f'{n}\n')
            f.write(f'{" ".join(list(map(str, lst)))}\n')

        subprocess.run(f'./out < {i}.in > {i}.out', shell = True)
        
# generate_sample_cases()
generate_random_cases()