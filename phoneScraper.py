#!/usr/bin/env python3
import re
import pyperclip
text = pyperclip.paste()
extractedPhonenumbers = re.findall(r"""
(
(\d{3}|\(\d{3}\))?          # Optional area code
(\s|-)                      # First seperator
(\d{3})                     # first 3 digits
-                           # Second seperator
(\d{4})                     # last 4 digits
((ext\.?\s|x){5})?          # Optional extension
)
    """, text, re.VERBOSE)

phoneNumbers = []
for phoneNumber in extractedPhonenumbers:
    phoneNumbers.append(phoneNumber[0])

print('\n'.join(phoneNumbers))

print(re.findall(r"""
\w*\.\w*@\w*\.\w{3}
    """, text, re.VERBOSE))
