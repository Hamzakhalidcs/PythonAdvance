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

# Generators can also receive the information from us, just like a normal function
def get_numbers(limit):
    for number in range(1, limit+1):
        if number%3==0:
            yield number

numbers = get_numbers(15)
for number in numbers:
    print(number)

# def get_square(limit):
#     return [number*number for number in range(1,limit+1)]

# numbers = get_square(5)
# print(numbers)

# def get_square(limit):
#     for number in range(1,limit+1):
#         yield number*number


# numbers = get_square(5)
# for number in numbers:
#     print(number)

def get_squares(limit):
    return (number * number for number in range(1, limit + 1))

numbers =get_squares(5)
for number in numbers:
    print(number)

# Now using yield from
def get_number():
    numbers= [1,2,3]
    yield from numbers

numbers = get_number()
for number in numbers:
    print(number)

"""
yield numbers means give me this one value, yield from numbers give me each 
value from numbers, one at a time
yield = produce values.
yield from = pass through/delegate values from another iterable or generator.
"""

def get_users():
    yield "Hamza"
    yield "Ali"


def get_admins():
    yield "Ahmad"
    yield "Usman"


def get_all_people():
    yield from get_users()
    yield from get_admins()


people = get_all_people()

for person in people:
    print(person)

# Generator pipeline(chaining generator)
def get_numbers():
    for number in range(1, 6):
        yield number


def get_squares(numbers):
    for number in numbers:
        yield number * number


numbers = get_numbers()
squares = get_squares(numbers)

for number in squares:
    print(number)