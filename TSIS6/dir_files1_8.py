"""#1
import os

path = '/Users/dino/Documents/GitHub/PP2'

print("Directories:")
for dirpath, dirnames, filenames in os.walk(path):
    for dirname in dirnames:
        print(os.path.join(dirpath, dirname))

print("\nFiles:")
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        print(os.path.join(dirpath, filename))

print("\nAll directories and files:")
for dirpath, dirnames, filenames in os.walk(path):
    for dirname in dirnames:
        print(os.path.join(dirpath, dirname))
    for filename in filenames:
        print(os.path.join(dirpath, filename))

#2
import os

path = '/Users/dino/Documents/GitHub/PP2/TSIS6/1.txt'

if os.path.exists(path):
    print("File exists")
    print('Exists:', os.access(path, os.F_OK))
    print('Readable:', os.access(path, os.R_OK))
    print('Writable:', os.access(path, os.W_OK))
    print('Executable:', os.access(path, os.X_OK))
else:
    print('File dont exists')

#3
import os

path = '/Users/dino/Documents/GitHub/PP2'

if os.path.exists(path):
    print("Path exists")
    print("\nFile name of the path:")
    print(os.path.basename(path))
    print("\nDir name of the path:")
    print(os.path.dirname(path))
else:
    print("Path dont exist")

#4

file = open("/Users/dino/Documents/GitHub/PP2/TSIS6/1.txt", 'r')
lines = len(file.readlines())
print(lines)

#5

file_path = '/Users/dino/Documents/GitHub/PP2/TSIS6/1.txt'

my_list = ['apple', 'banana', 'cherry', 'date']

with open(file_path, 'w') as file:
    for item in my_list:
        file.write(f"{item}\n")

print(f"The list has been written to the file '{file_path}'.")

#6
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for letter in alphabet:
    file_name = f"{letter}.txt"

    with open(file_name, 'w') as file:
        file.write(f"This is the file {file_name}.")
    
    print(f"File '{file_name}' has been created.")


#7

source_path = '/Users/dino/Documents/GitHub/PP2/TSIS6/1.txt'
destination_path = '/Users/dino/Documents/GitHub/PP2/TSIS6/2.txt'

with open(source_path, 'r') as source_file, open(destination_path, 'w') as destination_file:
    for line in source_file:
        destination_file.write(line)

print(f"The contents of '{source_path}' have been copied to '{destination_path}'.")
"""

#8
import os

file_path = '/Users/dino/Documents/GitHub/PP2/TSIS6/1.txt'

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"The file '{file_path}' has been deleted.")
    else:
        print(f"You do not have write access to '{file_path}'.")
else:
    print(f"The file '{file_path}' does not exist.")
