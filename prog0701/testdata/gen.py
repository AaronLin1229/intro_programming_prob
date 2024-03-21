import subprocess

for i in range(1, 30 + 1):
    with open(f"{i}.in", 'w') as f:
        f.write(f'{input()}\n')
    subprocess.run(f"python3 sol.py < {i}.in > {i}.out", shell = True)