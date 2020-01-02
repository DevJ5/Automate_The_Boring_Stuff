import pyperclip

print('This is a normal string, so it does it\'s escape')
print(r'This is a raw string, so it doesn\'t escape')
print("""Multi
Line""")
print('''Multi
Line''')

spam = "Hello"
print("He" in spam)
print("Oi" not in spam)
print(spam[-1])

# Strings immutable, so always return a new string:
spam.upper()
spam.lower()
spam.title()

spam.isupper() # Returns boolean
spam.islower()
spam.isalpha()
spam.isalnum()
spam.isdecimal()
spam.isspace()
spam.istitle()

spam.startswith("He")
spam.endswith("lo")

",".join(['cats', 'rats', 'bats'])

# Voorloopnullen
print(spam.rjust(10, "0"))
print(spam.ljust(10, "*"))
print(spam.center(11, "-"))

spam.strip()
spam.lstrip()
spam.rstrip()
print(spam.strip("Hlo")) # Strip these letters from both sides

spam.replace("e", "xyz")

print(pyperclip.paste())
pyperclip.copy("Hello world")



