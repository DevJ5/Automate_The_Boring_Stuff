import re
phoneNumber = "415-555-1011"
phonenumberRegEx = re.compile(r"\d\d\d")
# 1st way with findAll method, this will return all matches
print(phonenumberRegEx.findall(phoneNumber))
# 2nd way with search, this returns a match object on which we call the group method. This will just return the first match.
matchObject = phonenumberRegEx.search(phoneNumber)
print(matchObject.group())

# Grouping syntax
phonenumberRegEx = re.compile(r"(\d\d\d)")
matchObject2 = phonenumberRegEx.search(phoneNumber) # Notice the use of the raw string!
print(matchObject2.group(2))
