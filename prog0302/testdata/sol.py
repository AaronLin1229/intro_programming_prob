ch = input().strip()
if ch.isupper() and ch in "AEIOU":
    print(f"{ch} is class A")
elif ch.islower() and ch in "aeiou":
    print(f"{ch} is class B")
elif ch.isupper():
    print(f"{ch} is class C")
else:
    print(f"{ch} is class D")
