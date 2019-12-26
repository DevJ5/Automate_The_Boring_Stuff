arr = ['cat', 'rat', 'dog']

# Negative indexes count from the end, -1 is the last index.
print("There is a %s." % arr[-1])

# Ranges are done with a colon, from:to (but not include). Also called a slice.
print(arr[1:3]) # [rat, dog]
print(arr[:1])  # [cat]
print(arr[2:])  # [dog]

# Deleting an item in an array
del arr[2]

# Length of an array or string
print(len(arr))
print(len("hello"))

# Concatenate arrays or strings
arr2 = ['elephant', 'giraffe', 'bear']
print(arr + arr2)
print(arr * 3)
print("Hello " * 3)

# Typecast to a list
print(list("Hello"))

# Includes
print("rat" in arr)
print("cat" not in arr)

# Ranges
print(list(range(0,100, 2)))

# For loop
for i in range(0,5):
    print(i)

for j in range(len(arr2)):
    print("Index " + str(j) + ": " + arr2[j])

# Multiple assignments of array elements to variables
propertiesOfCat = ['fat', 'grey', 'stubborn']
size, color, mood = propertiesOfCat
print(size, color, mood)

# Swapping is easy in Python, no temp variable needed.
a = 10
b = 20
a, b = b, a
