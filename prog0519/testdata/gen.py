import random
import subprocess

def generate_sample_cases():
    sample = [(4, [2, 7, 11, 15], 9), (3, [3, 2, 4], 6)]
    for i, (n, lst, k) in enumerate(sample, 1):
        with open(f'sample{i}.in', 'w') as file:
            file.write(f"{n}\n")
            file.write(f"{' '.join(map(str, lst))}\n")
            file.write(f"{k}\n")
        subprocess.run(f'python3 sol.py < sample{i}.in > sample{i}.out', shell=True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        
        k = random.randint(-1e9, 1e9)
        num1 = random.randint(-1e9, 1e9)
        num2 = k - num1

        lst = [num1, num2]
        cannot_use = {num1, num2}

        n = random.randint(0, int(1e3) - 2)
        for _ in range(n):
            while True:
                this_num = random.randint(-1e9, 1e9)
                if this_num not in cannot_use: break
            
            lst.append(this_num)
            cannot_use.add(this_num)
            cannot_use.add(k - this_num)
        random.shuffle(lst)

        with open(f'{i}.in', 'w') as file:
            file.write(f"{len(lst)}\n")
            file.write(f"{' '.join(map(str, lst))}\n")
            file.write(f"{k}\n")
        subprocess.run(f'python3 sol.py < {i}.in > {i}.out', shell=True)

generate_sample_cases()
generate_random_cases()


