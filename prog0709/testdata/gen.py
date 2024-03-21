import random
import subprocess

def generate_sample_cases():
    sample = [
        (3, ["cat", "apple", "banana"]),
    ]
    for i, (n, strings) in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as file:
            file.write(f'{n}\n')
            for s in strings:
                file.write(f'{s}\n')
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 1000)
        strings = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 31))) for _ in range(n)]

        if i >= 25:
            while len(strings) < 900:
                strings.append(strings[random.randint(0, len(strings) - 1)])

        random.shuffle(strings)
        with open(f'{i}.in', 'w') as file:
            file.write(f'{len(strings)}\n')
            for s in strings:
                file.write(f'{s}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
