print("hello, world!")

a = str("Hello")
print(a, type(a))


b = str(""" Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""")

print(b)


print("### Strings are arrays ###")


print("The first letter of \"a\" is \"{}\"".format(a[0]))

print("### We can count the letters in a string ###")

num = 0

for x in a:
    num += 1

print("There are {} letters in \"a\" (Using loop)".format(num))

# or we can use length

print("There are {} letters in \"a\" (Using Length)".format(len(a)))

print("### We can check if there is a word in the string ###")

text = "Python is cool"

print("Is \"cool\" into \'text\"? {}".format(bool("cool" in text)))

# using "in" to find something returns bool (0, 1; false or true)

if "shit" not in text:
    print("No, \"shit\" is NOT present")