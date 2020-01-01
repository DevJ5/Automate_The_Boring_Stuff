pizzas = {
    "cheese": 9,
    "pepperoni": 10,
    "vegetable": 11,
    "buffalo chicken": 12
    }

for topping, price in pizzas.items():
    print(f"Pizza with {topping}, costs {price}.")
    print("Pizza with {0}, costs {1}.".format(topping, price))


# There is no order in dictionaries.

print('cheese' in pizzas) # True
print('ham' not in pizzas) # True 

# print(pizzas['ham']) # KeyError
# Solution:
if 'ham' in pizzas:
    print(pizzas['ham'])
# Alternative solution:
print(pizzas.get('ham', "doesnt exist"))

# There is also a setdefault method on dictionaries
message = '''It was a bright cold day in April when I parked my car.'''
count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] +=1

print(count)

print(pizzas.values())  # Returns a listlike datatype (dict_values)
list(pizzas.values())   # Returns list of values
list(pizzas.keys())     # Returns list of keys
list(pizzas.items())    # Returns list of tuples

for key in pizzas.keys():
    print(key)
