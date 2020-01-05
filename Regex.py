import re
phoneNumber = "415-555-1011"
phonenumberRegEx = re.compile(r"\d\d\d")
# 1st way with findAll method, this will return all matches
print(phonenumberRegEx.findall(phoneNumber))
# 2nd way with search, this returns a match object on which we call the group method. This will just return the first match.
matchObject = phonenumberRegEx.search(phoneNumber)
print(matchObject.group())

# Grouping syntax
phonenumberRegEx = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
matchObject2 = phonenumberRegEx.search(phoneNumber) # Notice the use of the raw string!
print(matchObject2.group(2))

batRegEx = re.compile(r"Bat(man|mobile|copter)", re.IGNORECASE)
print(batRegEx.findall("Batman lost a batmobile"))
matchObject3 = batRegEx.search("Batman lost a batmobile")
# Can return None as object
if matchObject3 != None:
    print(matchObject3.group(1))

