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

"""
 How does a dictionary find a key so quickly. suppose 
 students = {
    101: "Hamza",
    205: "Asad",
    310: "John",
    415: "Ali"
}
you might naturally ask : 
   How does python know where 310 is without checking 101, 205,then 310
   A hash function takes a key and produce a hash value. 
   conceptually key -> hash function -> hash value 
   so conceptually  310->hash function ->7 location ->7 "john"


Think of bucket 
Bucket
  0   → 
  1   →
  2   →
  3   →
  4   →
  5   →
  6   →
  7   → 310 : "John"
  8   →
  9   →

when python receive student[310], it hashes 310 and getsomething that helps idnentify the appropriate location. 

3: What about strings.
same goes for string value for example like dictionary is "hamza" :25, the same method will followed for that.  

4: Hash Collision 
Here where its get intersting. imaging our simplified hash function produces
310 ->7
415 ->7
Now two different key want the same bucket. 
Bucket 7
   ↓
310 : "John"
415 : "Ali"
This is called hash collision . 
Python dictionary has mechanisam to handle this situation.

thing to remember: 
    Different keys can produce the same hash-table location ,so dictionary lookup isn't mathemathically guranteed to
    be O(1) in every possible situation .That's why we say  O(1) average case rahter than O(1) always. 

The complexity depends not only on the data structure,but also on what operation you're performing on .

You now understand:

List index access → O(1)
List search → O(n)

Dictionary key lookup → O(1) average
Hash function → key → hash → location
Hash collision → two keys can map to the same location
Dictionary in checks keys, not values
"""