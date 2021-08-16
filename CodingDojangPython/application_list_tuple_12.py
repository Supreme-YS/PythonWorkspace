# tuple

a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

# this is not tuple comprehension, Generator!
b = (i for i in range(10) if i % 2 == 0)

print(b)
