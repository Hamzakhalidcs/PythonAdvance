"""
1 : String fundamentals 
  Indexing, slicing, Immutability

2: Common Operation 
  Split(), Join(), find(), replace(), count(), strip()

3: DSA Perspective 
    Searching a string O(n), Traversing Character, Comparing Strings, Build String Efficiently

4: Practice 
   Reverse a String, Check palindrome, count Characters, find duplicates, Basic String Problem


A string is a sequence of charactrers. 
Methods Implementartion. 
len()
.lower()
.upper()
.strip()
.split()
.find()
.count()
.replace()
"""

name = "Hamza"
print(name[0])
# negative indexing work 
print(name[-1])
print(name[::-1]) # : means start omitted : end omitted , -1 start from end 

# Strings are sequences of characters and list is a sequence of element.  
print(name[1:4]) 
""" 
Remember the slicing rule name[start:stop], the start is include and the exit is exclude. 
Strings are immutable. name[0] = "A" does not support this assignment operation. 
you can get the same result by using 
"""
new_name = "A" + name[1:]
print(new_name)
print(len(name))

word  = "Python Programming"
print(word.lower())
print(word.upper())
print(word[7:18])
print(word[::-1])      

"""
 Important DSA pattern emerging 
 Does Python need to process every element ?
 if yes, it's often O(n)

 len(word)        O(1)
 word[3]          O(1) 
 word.lower()     O(n)
 word[::-1]       O(n)

"""

sentence  = "Python is easy to learn"
print(sentence.split())

join_word = ["python", "is", "easy"]
print(" ".join(join_word))      # " " this is seprator we want to put in between element

date_join = ["2026", "08", "25"]
print("-".join(date_join))

"""
Thing to remember
split changes string -> list
join() changes list -> string

So  split() -> O(n) and join() -> O(n)
where n represent the amount of input/output text being processed. 
"""