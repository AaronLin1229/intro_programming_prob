import random
import subprocess

def generate_sample_cases():
    sample = ["(())()()", "(()))"]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(data)
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 500)
        s = ''
        for _ in range(n):
            r = random.randint(0, len(s))
            s = s[: r] + "()" + s[r: ]

        if random.choice([True, False]) == False:
            lst = list(s)
            random.shuffle(lst)
            s = "".join(lst)

        with open(f'{i}.in', 'w') as f:
            f.write(s)
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

            

generate_sample_cases()
generate_random_cases()
