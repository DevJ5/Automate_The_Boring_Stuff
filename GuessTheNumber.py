import random

print("Hello. What is your name?")
name = input()
minNumber = 1
maxNumber = 20
randomNumber = random.randint(minNumber,maxNumber)
print("Well, {}, I am thinking of a number between {} and {}".format(name, minNumber, maxNumber))
print(randomNumber)
# Ask the player to guess a maximum of 6 times
for guessesTaken in range(1,7):
	print("Take a guess")
	guess = int(input())
	if guess < randomNumber:
		print("Thats too low")
	elif guess > randomNumber:
		print("Thats too high")
	else:
		break


# no block scope within loops
if guess == randomNumber:
	print("Yay, correct! The number was %s." % randomNumber)
else:
	print("You have guessed 6 times and didnt get it right. Better luck next time!")
