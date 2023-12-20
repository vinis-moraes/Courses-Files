# Data Types

print("Welcome to the program!")

# Text

text = str("This is a string (Text)")
print(text)

# Numbers

num1 = int(12)
print("Number (Integer): {}".format(num1))
num2 = float(3.14)
print("Number (Float): {}".format(num2))
num3 = complex(1j)
print("Number (Complex): {}".format(num3))

# Sequence Types

st1 = list(["Apple", "Banana", "Cherry"])
print("List: {}".format(st1))
st2 = tuple(("Apple", "Banana", "Cherry"))
print("Tuple: {}".format(st2))
st3 = range(6)
print("Range: {}".format(st3))

# Mapping Types

mp1 = dict({"name" : "John", "age" : 36})
print("Dict: {}".format(mp1))

# Set Types

st1 = set({"Apple", "Banana", "Cherry"})
print("Set: {}".format(st1))
st2 = frozenset({"Apple", "Banana", "Cherry"})
print("Frozenset: {}".format(st2))

# Boolean

boolean = bool(True)
print("Boolean: {}".format(boolean))

# Binary Types

bt1 = bytes(b"Hello")
print("Bytes: {}".format(bt1))
bt2 = bytearray(5)
print("Bytearray: {}".format(bt2))
bt3 = memoryview(bytes(5))
print("Memory View: {}".format(bt3))

# NoneType

nt = None
print("NoneType: {}".format(nt))