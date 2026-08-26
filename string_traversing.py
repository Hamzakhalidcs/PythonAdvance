"""
String traversing is the process of going through the characters of string one by one.
time complexity is O(n), because if there are n element so it have to loop process for n times.

Enumeration ofte called enum is a way to define a set of named constant values.It allows you to 
group related constants together under a single type, making your code more meaningful and less error prone.
"""

word = "FootBall"
for char in word:
    print(char)


# same can do using index & specially for to find the character with index number.
for i in range(len(word)):
    print(i, word[i])

# enumerate 
for i, char in enumerate(word):
    print(i, char)


# Characet Frequency 
frequency = {}
text = "banana"


for char in text:
    if char in frequency:
        frequency[char] +=1
    else:
        frequency[char] = 1

print("This is simple for loop result")
print(frequency)

# same can do with professionally and use .get function to make dictionary

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("This is with .get funciton result")
print(frequency)

# Now we have to find the frequency of first non repeat character 


word_frequency = {}
traversed_word = "swiss"

for char in traversed_word:
    word_frequency[char] = word_frequency.get(char, 0) + 1

for char in traversed_word:
    if word_frequency[char] == 1:
        print(char)
        break

# make this in to function to re use this again and again 
def first_non_repeating(word):
    word_frequency ={}

    for char in word:
        word_frequency[char] = word_frequency.get(char, 0) + 1

    for char in word:
        if word_frequency[char] == 1:
            return char
        
    return None

print(first_non_repeating("Hamza"))
            

# A Palindrome is a string that read the same forward and backward. e.g madam
palindrome_word = "level"
print(palindrome_word[::-1])
palindrome_word = palindrome_word[::-1]
print(palindrome_word)

word_list = ["madam", "level", "python", "racecar"]
for word in word_list:
    if word == word[::-1]:
        print(word, "Is Palindrome")
    else:
        print(word, "Not palindrome")

# The time compelxity is O(n) but space is O(n) as it have to create new string while using ::-1
# so use two pointer approach to use less space and time 

def is_palindrome(word):
    left = 0
    right = len(word)-1

    while left < right:
        if word[left] != word[right]:
            return False
        
        left +=1
        right -=1
    
    return True

print(is_palindrome('madam'))

def reverse_list(word_list):
    left = 0 
    right = len(word_list) -1 
    while left < right:
        word_list[left], word_list[right] = word_list[right], word_list[left]
        
        left += 1
        right -=1

    return word_list

test_list = ["H", "a", "m", "z", "a"]
print("Orignal List")
print(test_list)

print(reverse_list(test_list))