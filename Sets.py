# Sets don't care about order and they only contain uniques.
courses = {'History', 'Math', 'Math', 'Physics', 'CompSci'}
print(courses)

# Sets are optimized for membership tests (i.e. does the set contain the item)
print('Math' in courses)

# Intersections
courses2 = {'Physics', 'CompSci', 'Design'}

print(courses.intersection(courses2))

# Difference
print(courses.difference(courses2))

# Union
print(courses.union(courses2))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

