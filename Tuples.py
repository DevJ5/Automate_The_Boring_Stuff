# Lists are mutable and use square brackets
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[1] = 'Not Math'

print(list_1)
print(list_2)

print("--------------------------------------------------")
# Tuples are lists that are immutable and use parentheses
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[1] = 'Not Math'

print(tuple_1)
print(tuple_2)

