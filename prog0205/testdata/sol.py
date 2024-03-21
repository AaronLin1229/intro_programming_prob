# Read input
a, b = map(int, input().split())
c, d = map(int, input().split())

# Calculate determinant
determinant = a*d - b*c

# Print output
print(determinant)
