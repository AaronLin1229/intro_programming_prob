import random
import subprocess

def generate_sample_testcases():
    samples = [
        ([1.0, 2.0, 3.0, 4.0, 5.0], "sample1"),
        ([10.5, 15.5, 20.5], "sample2")
    ]
    for arr, name in samples:
        with open(f"{name}.in", "w") as f:
            f.write(f"{len(arr)}\n")
            f.write(" ".join(map(str, arr)))

def generate_random_testcases(num_cases=30):
    for i in range(1, num_cases + 1):
        n = random.randint(1, 1000)
        
        with open(f"{i}.in", "w") as f:
            f.write(f"{n}\n")
            f.write(" ".join(f"{x:.15f}" for x in arr))

generate_sample_testcases()
generate_random_testcases()
