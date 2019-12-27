arr = ['cat', 'rat', 'dog']

# Negative indexes count from the end, -1 is the last index.
print("There is a %s." % arr[-1])

# Ranges are done with a colon, from:to (but not include). Also called a slice.
print(arr[1:3]) # [rat, dog]
print(arr[:1])  # [cat]
print(arr[2:])  # [dog]

# Adding item to end of array
arr.append("beaver")

# Deleting an item in an array
del arr[3] # or arr.remove("beaver")


# Adding item to an index of an array
arr.insert(0, "beaver")

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

# Sorting is done by ascii codes. Uppercase comes before lowercase
arr.sort()
arr.sort(reverse=True)
arr.sort(key=str.lower) # Now its true alphabetical order instead of ascii code

# Strings and lists are similar
print(list("Hello"))
name = "Ernie"
print(name[:2])
print("xxx" in name)

# Strings are immutable
try:
    name[5] = "s"
except Exception as e:
    print("This will give an error" + str(e))

# To copy a list
import copy
spam = ["a", 
        "b",
        "c",
        "d"]

copyRefSpam = spam
deepCopy = copy.deepcopy(spam)
print(copyRefSpam == spam) # True, cause pointer.
print(deepCopy == spam) # True, cause the lists contain the same values.
print(deepCopy is spam) # False, because they are in different memory addresses.

