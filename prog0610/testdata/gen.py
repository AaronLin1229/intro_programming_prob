import random
import subprocess

def generate_sample_cases():
    for i in range(1, 2 + 1):       
       subprocess.run(f'./out < sample{i}.in > sample{i}.out', shell = True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 100)
        if i <= 3: n, m = 2, 2
        mtx = [[random.randint(0, 1) for j in range(n)] for i in range(n)]
        k = random.randint(1, 100)

        with open(f"{i}.in", "w") as f:
            f.write(f"{n}\n")
            for lst in mtx:
                f.write(f"{' '.join(list(map(str, lst)))}\n")
            f.write(f'{k}\n')

        subprocess.run(f'./out < {i}.in > {i}.out', shell = True)

generate_sample_cases()
generate_random_cases()