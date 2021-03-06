import os
from datetime import datetime
# To print the methods of a module
print(dir(os))

# Get current working directory
print(os.getcwd())
# Change current working directory
os.chdir("D:\Computer_Science\Python")
print(os.getcwd())
# List all the directory contents
print(os.listdir())

# Create folder
# os.makedirs("hoihoi") # This creates new subfolders as well if the path doesnt exist.
# os.mkdir("hoihoi") # This will give an error if the subfolder doesnt exist.

# Remove folder
# os.rmdir("hoihoi") # This is safer to use, because it doesnt remove subfolders in the path.
# os.removedirs("hoihoi")

# Rename folder or files
# os.makedirs("hoihoi")
# print(os.listdir())
# os.rename("hoihoi", "byebye")
# print(os.listdir())

# Show info
print(os.stat("byebye"))
"""
os.stat_result(st_mode=16895, st_ino=2083196302635571266, st_dev=2330088584, st_nlink=1, st_uid=0, st_gid=0, st_size=0, 
               st_atime=1578243401, st_mtime=1578243401, st_ctime=1578243401)
"""
mod_time = os.stat("byebye").st_mtime
print(datetime.fromtimestamp(mod_time))

# Walk the directory tree from a certain directory.
"""
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files", filenames)
    print()
"""

# Environment variables
# print(os.environ)
print(os.environ.get('USERPROFILE'))
# Create a file in a certain path. Use path.join to prevent guesses of backslashes in filepaths.
file_path = os.path.join(os.environ.get('USERPROFILE'), 'test.txt') 
print(file_path)

with open(file_path, 'w') as f:
    f.writelines("Something something")

# Check existance of a file, it doesnt exist, create it. 'a' gets used for appending.
# if not os.path.exists('/tmp/test'):
#    with open('/tmp/test', 'w'): pass

# Prints the filename
print(os.path.basename("/tmp/test.txt"))
# Prints the direcotry
print(os.path.dirname("tmp/test.txt"))
# Print both
print(os.path.split("tmp/test.txt"))

# Prints out if the path exists
os.path.exists('/tmp/test.txt')
# Check if its a directory
print(os.path.isdir(""))
# Check if its a file
print(os.path.isfile(""))

# Print the filepath and extension seperately
print(os.path.splitext('/tmp/test.txt'))

# Get the absolute path from a relative path (from the current working directory)
print(os.path.abspath("test.txt"))

# Get the size of all files in the current directory
totalSize = 0
for file in os.listdir():
    if not os.path.isfile(file):
       continue
    else:
        totalSize += os.path.getsize(os.path.abspath(file))   


