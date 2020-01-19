import shutil
# shutil.copy('C:\\Users\\veens\\Desktop\\todo.txt', 'C:\\Users\\veens\\Desktop\\todo2.txt')
# shutil.copytree('C:\\Users\\veens\\Desktop\\myfolder', 'C:\\Users\\veens\\Desktop\\myfolder2')
# shutil.move('C:\\Users\\veens\\Desktop\\myfolder2\\todo.txt', 'C:\\Users\\veens\\Desktop\\todo.txt')

import os
os.chdir('C:\\Users\\veens\\Desktop')
print(os.listdir())
for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)
# print(os.getcwd())
# os.unlink('todo.txt')

# os.rmdir('myfolder') # removes empty directory
# shutil.rmtree('myfolder')

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    print(folderName, subfolders, filenames)
    #if 'myfolder2' in subfolders:
    #    shutil.rmtree('myfolder2')