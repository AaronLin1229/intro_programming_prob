def fahrenheit_to_celsius(F):
    return (F - 32) * 5 / 9

F = float(input())
C = fahrenheit_to_celsius(F)
print(C)
