# https://realpython.com/python-requests/
import requests, os

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
# Content is bytes
print(res.content[:10])
# Text is a string
print(res.text[:10])
#with open(os.getcwd()+"\..\\rj.txt", 'w') as f:
#    f.write(res.text[:100])
# Status code
print(res.status_code)

# Writing bytes
with open(os.getcwd()+"\..\\rj.txt", 'wb') as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)