import random
import string
import subprocess

def gen(s, _k):
    return "".join(random.choices(s, k = _k))

def generate_plate():
    valid_characters = string.ascii_letters + string.digits
    non_chars = "!@#$%^&*()_+=[];\':\"<>,.?/\\"

    ver = random.randint(1, 3)
    if random.choice([True, True, True, True, True, True, True, False]): base = valid_characters
    else: base = valid_characters + non_chars

    if ver == 1:
        s = gen(base, 2) + "-" + gen(base, 4)


    elif ver == 2:
        s = gen(base, 3) + "-" + gen(base, 3)

    else:
        s = gen(base, 7)
    
    return s


def main():
    for i in range(1, 30 + 1):
        n = random.randint(1, 30)
        lst = [generate_plate() for _ in range(n)]
        with open(f"{i}.in", "w") as f:
            f.write(f"{len(lst)}\n")
            for plate in lst:
                f.write(f"{plate}\n")
        
        subprocess.run(f"./out < {i}.in > {i}.out", shell = True)

if __name__ == "__main__":
    main()
