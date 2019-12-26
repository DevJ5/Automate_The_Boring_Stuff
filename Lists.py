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
