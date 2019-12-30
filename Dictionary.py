pizzas = {
    "cheese": 9,
    "pepperoni": 10,
    "vegetable": 11,
    "buffalo chicken": 12
    }

for topping, price in pizzas.items():
    print(f"Pizza with {topping}, costs {price}.")
    print("Pizza with {0}, costs {1}.".format(topping, price))


