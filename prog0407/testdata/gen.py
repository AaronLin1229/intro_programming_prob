import random
import subprocess

primes = [
    902761, 894403, 999983, 997259, 994559,
    802661, 850933, 855601, 950009, 952439,
    982643, 980599, 982703, 974419, 966221
]
ptr = 0

def generate_samples():
    samples = [
        (5, "YES"),
        (4, "NO")
    ]
    for i, (inp, out) in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as infile:
            infile.write(f'{inp}\n')
        with open(f'sample{i}.out', 'w') as outfile:
            outfile.write(f'{out}\n')

def generate_random():
    for i in range(1, 30 + 1):
        if i == 1: n = 0
        elif i == 2: n = 1
        elif i <= 17: n = primes[i - 3]
        else: n = random.randint(1, 10**6)
        with open(f'{i}.in', 'w') as infile:
            infile.write(f'{n}\n')
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_samples()
generate_random()
