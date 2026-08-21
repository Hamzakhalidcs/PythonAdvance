student= {
    1: "Hamza",
    2: "Asad", 
    3: "Umar"
}

"""
 Dictionary is key->value pair
 important Question, why is looking up a dicitonary key usually much faster than searching a list .

 Dont think dicionary operation are always O(1)
 That's too absolute. The more accurate is 
 Dicitionary lookup, insertion and deletion are O(1) on average. 
 Just to remember
 List search by value/key -> O(n)
 dictionary lookup by key -> O(1) average 
""" 

print(2 in student)