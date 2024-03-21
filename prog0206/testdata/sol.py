a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

# Inner product
inner_product = a*d + b*e + c*f
print(inner_product)

# Cross product
x = b*f - c*e
y = c*d - a*f
z = a*e - b*d
print(x, y, z)
