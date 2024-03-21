import random
import subprocess

def generate_sample_cases():
    samples = [
        "00001234",
        "00012321000",
        "000000"
    ]
    for i, data in enumerate(samples, 1):
        with open(f'sample{i}.in', 'w') as f_in, open(f'sample{i}.out', 'w') as f_out:
            f_in.write(data)
        subprocess.run(f"./out < sample{i}.in > sample{i}.out", shell = True)

def generate_random_cases(num_cases=30):
    for i in range(1, num_cases + 1):
        num_zeros = random.randint(0, 511)
        num_digits = random.randint(0, 512)
        leading_zeros = "0" * num_zeros
        digits = ''.join(list(random.choice("123456789")) + list(random.choices("0123456789", k=num_digits - 1)))
        data = leading_zeros + digits

        with open(f'{i}.in', 'w') as f_in, open(f'{i}.out', 'w') as f_out:
            f_in.write(data)
        
        subprocess.run(f"./out < {i}.in > {i}.out", shell = True)
        

generate_sample_cases()
generate_random_cases()
