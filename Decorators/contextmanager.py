# """
# A context Manager is a mechanisam that handles setup and clean autmatically.
# The most familar example is opening a file 
# """
# with open("../note.txt", "r") as file:
#     data = file.read()
#     # raise Exception("Something went wrong")
#     print(data)

# print(file.closed)  # to check whether the file is closed or not. 

# class MyContext:
#     def __enter__(self):
#         # print("Entering Context")
#         return 100

#     def __exit__(self, exc_type, exc_value, traceback):
#         # exc_type what kind of error happend,
#         #  exc_value contains the actual exception object, including its message
#         # trace_back where did the error happened. 
#         print("Leaving Context")
#         return False

# with MyContext() as number:
#     print(number) 

# # with MyContext():  # Create an object/instance of this class
#     # print("Inside Context")
#     # raise ValueError("Something went wrong")

with open("../note.txt", "r") as file:
    print(file.closed)

print(file.closed)


