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

# Without precompiling the regex:
print(re.match("Bat(wo)?man", "Batman"))
print(re.search("Bat(wo)*man", "Batman") == None)
print(re.findall("Bat(wo)+man", "Batwoman"))

# Non greedy (means matching the shortes string possible, with ? after curly braces):
print(re.match("\d{3,5}?", "1234567890"))

# .* means all but not newline chars, to add those as well use second argument re.DOTALL
dotStar = re.compile(r".*", re.DOTALL)
print(dotStar.search("Hello\nWorld!"))

# Find and replace using sub method
namesRegex = re.compile(r"Agent \w+")
print(namesRegex.sub("***", "Agent Bob is on duty and so is Agent Alice"))

# Replace with parts of the original group (use raw string because of \1 for group)
namesRegex2 = re.compile(r"Agent (\w)\w*")
print(namesRegex2.sub(r"\1***", "Agent Bob is on duty and so is Agent Alice"))




