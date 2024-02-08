import random

x = 1 # int 
y = 2.8 # float
z = 1j # complex ("j" is the imaginary part)

print("x = {} (Integer)".format(x))
print("y = {} (Float)".format(y))
print("z = {} (Complex)" .format(z))

# Type Conversion

print("### Converting Types ###")

print("{}".format(float(x)))
print("{}".format(int(y)))
print("{}".format(complex(x)))

# Complex Numbers cannot be converted


# Random Number

print("### Generating a random number... ###")

print("{}".format(random.randrange(1,50)))