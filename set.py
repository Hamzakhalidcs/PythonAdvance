"""
A Python set is a collection that stores unique values . 
one thing to rememeber (A set always prevent duplicate values)
"""

number = {10,20,30,40,50}

number.add(20)

print(number)

# Why would we use set,suppose 
students = ["Hamza", "Asad", "Hamza", "John", "Asad"]

unique_student = set(students)
# Result will ("Hamza", "Asad", "John")

"""
Sets are Collection of unique values.
no index-based access 
duplicate automatically removed 
membership O(1) average. 
Easiest things to remember in sets 
set with values {}
Empty set set()
Tuple()
Important Functions 
Union
Intersection 
difference 
Symetric_difference
"""

# Checking the union 
A= {1, 2, 3, 4, 5}
B ={3, 4, 5, 6, 7}

print(A.union(B))

# Intersection only the elements that exist in both sets. 
print(A.intersection(B))

# Difference (Give me the element that are in A not in B) As A-B =! B-A 
print(A-B)

# Symetric Difference (Elements that are in A or B, but not in both) A^B 

print(A.symmetric_difference(B))

python_student = {"Hamza", "Asad", "Ali", "John"}
sql_student = {"Asad", "Ahmad", "John", "Bilal"}
# Student who know both 
print(python_student & sql_student)

print(python_student - sql_student)

# One important DSA point (Dont Assume every set Operation O(1))
# for example (A&B) has to process element from the sets, so it complexity depend on the size of the sets. 