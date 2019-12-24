def askUserInput():
    while True:
        try:
            print("What is your age?")
            age = int(input())
            return age
        except ValueError:
            print("Not a valid input...")

def printAge(age):
    try:
        print("Your age is " + age + ".")
    except:
        print("Cant put integer in there")

age = askUserInput()
printAge(age)