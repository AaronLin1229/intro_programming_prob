import random
import subprocess

def generate_sample_cases():
    sample = [
        ([5, -1, 2, 3, -4, 5], "3 2\n"),
        ([4, -3, -2, -1, 0], "0 3\n")
    ]
    for i, data in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as f_in, open(f'sample{i}.out', 'w') as f_out:
            n, arr = data[0][0], data[0][1:]
            f_in.write(f"{n}\n")
            f_in.write(' '.join(map(str, arr)) + "\n")
            f_out.write(data[1])
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 10**4)
        arr = [random.randint(-10**9, 10**9) for _ in range(n)]
        
        for j in range(n):
            arr[j] = random.choice([arr[j], arr[j], arr[j], 0])

        with open(f'{i}.in', 'w') as f:
            f.write(f"{n}\n")
            f.write(' '.join(map(str, arr)) + "\n")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()