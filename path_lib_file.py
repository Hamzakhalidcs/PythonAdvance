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

path_object = Path("note.txt")

print(path_object.exists())  # Check if the file exists

if path_object.exists():
    print(f"File '{path_object.name}' exists at: {path_object.resolve()}")
else:
    print(f"File '{path_object.name}' does not exists.")

# Now for checking the name is file or directory 
print(path_object.is_file())  # True if it's a file, False otherwise


# now if this is file so print this is file not true or false 
if path_object.exists() and path_object.is_file():

    print(f"'{path_object.name}' is a file.")

else:
    print(f"'{path_object.name}' is not a file.")


print(path_object.is_dir())   # True if it's a directory, False otherwise

if path_object.exists() and path_object.is_dir():
    print(f"'{path_object.name}' is a directory.")

else:
    print(f"'{path_object.name}' is not a directory.")


# path.mkdir()  # Create a new directory
new_path_object = Path("Backup")
new_path_object.mkdir(exist_ok=True)  # Create a new directory if it doesn't exist
print("Program Continue Running...")


# if not new_path_object.exists():
#     new_path_object.mkdir()
#     print(f"Directory '{new_path_object.name}' created.")

# else:
#     print(f"Directory '{new_path_object.name}' already exists.")

# exists=True parameter tell python if the directory already exists, don't raise an error.just conitunue
# runiing the program. 

# Now move to parents=ok if directly backup/july/2026 give error of no folder exists, to overcome
parent_path = Path("Data/Employees/july")

# python thinks like
#  data needed ? create it,
#  Employees needed ? create it,
#  july needed ? create it.

parent_path.mkdir(parents=True, exist_ok=True)  # Create nested directories if they don't exist

# ranaming the file using pathlib 
path_1 = Path("abc.txt")
new_path = Path("ABC.txt")

path_1.rename(new_path)  # Rename the file

new_path_move = Path("Backup/ABC.txt")
path_1.rename(new_path_move)  # Move and rename the file to a new location

# back_up_path  = Path("reports/sales.csv")
# new_name_path = Path("Backup/salesBackup.csv")
# back_up_path.rename(new_name_path)  # Rename and move the file to a new location


"rename() needs a destination path so Python knows what the file or directory should be renamed to."

"""One sentence to remember forever

Relative Path

"Start from where I am now."

Absolute Path

"Go to this exact location."""""