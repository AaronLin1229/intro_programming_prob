import random
import subprocess

def generate_sample_cases():
    sample = [("madam", "YES"), ("hello", "NO")]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f:
            f.write(data[0])
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        ver = random.choice([True, False])
        if ver == True:
            hlf_len = random.randint(1, 5 * 10**2)
            if random.choice([True, False]):
                s1 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=hlf_len))
                s2 = s1[::-1][1:]
                s = s1 + s2
            else: 
                s1 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=hlf_len))
                s2 = s1[::-1]
                s = s1 + s2
        else:
            length = random.randint(1, 10**3)
            s = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))
        
        with open(f'{i}.in', 'w') as f:
            f.write(s)
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()
