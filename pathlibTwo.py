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