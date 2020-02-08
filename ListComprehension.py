numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([item for item in numbers if item % 2 == 0])

print(list(map(lambda n: n + 1, numbers)))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("    Bert", "SeSAMstreet   "))

print([(n, c) for n in range(4) for c in "abcd"])

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)
