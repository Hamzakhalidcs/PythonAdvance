import os 

print("Current working directory:", os.getcwd())

# so when we type  with open("file.txt", "r") as file:
# Python will look for file.txt in the current working directory, which is the directory from 
# which the script is being run.It looks inside the current working directory. 
# There are two types of path in python. 1. Absolute path 2. Relative path
# with open will look for the file in the current working directory. 

# with open("D:\\PythonAdvanced\\studentManagement\\library_books.txt")
# here you telling the python the exact location of the file. 

print(os.listdir())  # List all files and directories in the current working directory

# print wit out list 
for file in os.listdir():
    print(file)


# len(os.listdir())

# # creating a new directory
try:
    os.mkdir("backup")
except FileExistsError:
    print("Directory 'backup' already exists.")

# checking the file exist or not 
print(os.path.exists("backup"))

# checking if this is file or not
print(os.path.isfile("backup"))  # False, because 'backup' is a directory

# checking if this is directory or not 
print(os.path.isdir("backup"))  # True, because 'backup' is a directory

# if os.path.exists("backup"):
    # load book
# else:
   #start with empty library

#This is called defensive programming. You check if the file or directory exists 
# before performing operations on it to avoid errors.

# rename a file or directory
os.rename("backup", "backup_renamed")   

# deleting a file or directory
os.remove("backup_renamed")  # Uncomment to delete the file

# this is only use for deleting the files not directories.