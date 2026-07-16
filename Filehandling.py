# file = open('note.txt', 'r')

# print(file.readline())

# print(file.read())

# file.close()


with open ('note.txt', 'r') as file:
    print(file.readline())
    print(file.read())


    