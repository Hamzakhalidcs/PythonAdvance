from pathlib import Path

path1 = Path("note.txt")
# print(path1.exists())

# path.iterdir() is important as it will use in data analysis, webautomation, web Scraping,
# ETL, backendDevelopment, and AI Projects. 

# this method is use return and iterator that contains all the fields and folder inside directory.
# One thing to remember,it does not go inside the subdiretories,only list the immediate contents of directory)

folder = Path("reports")

for item in folder.iterdir():
    print(item.name)

practice_path = Path("practice")

for file in practice_path.iterdir():
    if file.is_file():
        print(file.name)

# path_object = Path("Documents/Resume.pdf")
# path_object.mkdir(parents=True,exist_ok=True)

path_object = Path("Documents/Resume.pdf")

print(path_object.name)

# .stem will use to get the name of file without extension
print(path_object.stem)

print(path_object.suffix)  # .suffix will use to get the extension of file

# Trying to pushing some stuff

# trying suffixes methods 
path = Path("database.backup.sql")
print(path.suffixes)


# getting CWD
print(Path.cwd())

current = Path.cwd()
print(current)
print(type(current))

print(isinstance(current, Path))

# Path.home returns the home directory of the current user . 

home = Path.home()
print(home)
print(home.is_dir())

# path.home() allow us to get current user's home directory without hardcoding the username,  and then we 
# easily make the build paths relative to home direcory.
# difference b/w path.cwd and home is return current working directory and files realative to where your program
# running , path.home is user home directory , user specific folder like desktop , documents,downlods

#  path.touch creates an empty file if it does ont exists 
path = Path("Abc.txt")
# path.touch()

file = Path("ABC.txt")
file.touch()

print(file.exists)

log_file = Path("application.log")
if not log_file.exists():
    log_file.touch()

print("Ready to write logs")

file1 = Path("practice.txt")
print(file1.exists())
file1.touch()
print(file1.exists())

# we can do the same job using write_text method even if the file not exists
report_file = Path("report_file.txt")
report_file.write_text("Hello the world of the Python")

# glob method searches for files and folders that match a pattern . i.e find every thing that matches the rule 
glob_path = Path("practice")
for file in glob_path.glob("*.txt"):
    print(file)


# rglob methods searches for files inside of folder as well ,like in folder there is another folder, it will search
r_glob_path = Path("practice")

for file in glob_path.rglob("*.txt"):
    print(file) 

# Path.read_text() reads the entire content of a text file and return as a string . 
file = Path("note.txt")
content = file.read_text()
print(type(content))

# file.write_text("Only Python")
print(content)

# it does not return a path object, it returns a string,because you have read the text from file in to memory.
# file.touch and write_text if it not exist touch is not required it will do the job .

# Path.read_bytes() and path.write_bytes(), works with binary data .
img_path  = Path("practice/images.png")
data  = img_path.read_bytes()  
print(type(data))     #class str byte

print(data)   #print b'' means byte object 
