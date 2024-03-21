import random
import subprocess

def generate_sample_cases():
    sample = [
        ([1, 2, 1, 2, 3], "sample1"),
        ([4, 4, 6], "sample2")
    ]
    for i, (data, filename) in enumerate(sample, 1):
        with open(f'{filename}.in', 'w') as file:
            file.write(f"{len(data)}\n")
            file.write(' '.join(map(str, data)))
        subprocess.run(f'python3 sol.py < {filename}.in > {filename}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 499)
        
        s = set()
        for j in range(n):
            while True:
                this_num = random.randint(1, 1e9)
                if this_num not in s: break
            s.add(this_num)
        while True:
            unique_num = random.randint(1, 1e9)
            if unique_num not in s: break
        
        pool = list(s) + list(s) + [unique_num]
        random.shuffle(pool)

        with open(f'{i}.in', 'w') as f:
            f.write(f"{2 * n + 1}\n")
            f.write(' '.join(map(str, pool)))

        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
