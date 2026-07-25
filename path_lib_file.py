# pathlib is a built-in python module that provides an object-oriented way
# to work with file and directory paths.
# In simple words, pathlib allows us to create , access, rename, delete and manipulate files 
# and folders more easily than the os module. 

# from pathlib import Path 

# file = Path("note.txt")  # Create a Path object for the file "note.txt"

# print(file.exists())  # Check if the file exists


from pathlib import Path

# path_object= Path("D://PythonAdvanceD")  # Create a Path object for the file "report.txt"

# print(path_object.exists())  # Check if the file exists

path_object = Path("notes.txt")

print(path_object.exists())  # Check if the file exists

if path_object.exists():
    print(f"File '{path_object.name}' exists at: {path_object.resolve()}")
else:
    print(f"File '{path_object.name}' does not exists.")

