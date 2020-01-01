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

print(pizzas.values())  # Returns a listlike datatype (dict_values)
list(pizzas.values())   # Returns list of values
list(pizzas.keys())     # Returns list of keys
list(pizzas.items())    # Returns list of tuples

for key in pizzas.keys():
    print(key)
