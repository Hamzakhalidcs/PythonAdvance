"""
A generator is a function that produce a sequence of values one at a time,on demand,
instead of computing them all at once and storing them in memory. 
forloop = how we iterate 
Generator = how we store/produce the values while iterating.
Generator becomes especially valuable as the data gets large or when data is large or when its
comes continiously,such as large files, datbases cursor, API stream or log stream. 
yield allows the generator to produce a value one at a time when requested, while remembring 
where it stopped. 
"""
def get_numbers():
    for number in range(1, 6):
        yield number
        print("I am Continuing")

numbers= get_numbers()
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
for number in numbers:
    print(number)


# def get_user():
#     for user_id in range(1, 1000):
#         yield user_id

# def process(data):
#     print("Processing User", data)

# users = get_user()

# for data in users:
#     process(data)

def get_users():
    users= [
        {"name": "Hamza", "age":29},
        {"name": "Ali", "age":35},
        {"name":"Ahmad", "age":32}
    ]
    for user in users:
        yield user

def process_get_users(data):
    print(f"{data['name']} is {data['age']} years old")

users = get_users()
for data in users:
    process_get_users(data)