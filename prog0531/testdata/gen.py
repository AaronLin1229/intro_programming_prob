import random
import subprocess

def mtx_to_str(mtx):
    s = ''
    for lst in mtx:
        s += " ".join(list(map(str, lst))) + '\n'
    return s

def gen_mtx(m):
    return [[random.randint(0, 1) for j in range(m)] for i in range(m)]

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        n, m = random.randint(2, 20), random.randint(1, 16)
        q = random.randint(0, 1000)

        with open(f"{i}.in", "w") as f:
            f.write(f"{n} {m}\n")
            for j in range(n): 
                f.write(f'{random.randint(0, 1)}\n')
                f.write(f"{mtx_to_str(gen_mtx(m))}")
                f.write(f'\n')

            f.write(f"{q}\n")
            for j in range(q):
                f.write(f"{mtx_to_str(gen_mtx(m))}")
                if j != q - 1: f.write(f'\n')
        
        subprocess.run(f"./out < {i}.in > {i}.out", shell=True)
        

# generate_sample_cases()
generate_random_cases()