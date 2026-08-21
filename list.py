number = [10,20,30,40,50]
# A list is order and index based i.e index 0 :10 and so on, and negative index like -1 will start from last

print(number[0])
print(number[-1])

# How expesnive is an operation
# for example number[3] can directly access to index 3, meaning the operation takes same amount of work 
# whether its 10 element list or 10 million element list but consider  
number.insert(0,99)

# now python have to make room for 0 index and shift all index forward, that's more work as the list grow.
# This is where Big O starts 

"""
Our first mini-table
Operation	        Typical complexity
numbers[i]	            O(1)
numbers.append(x)	    O(1) amortized
numbers.insert(0, x)	O(n)
numbers.pop()	        O(1)
numbers.pop(0)	        O(n)
Search x in numbers	    O(n)
"""

"""
 Now make them concrete, imagine 10 elements , inserting at the begining means to move 10 elements 
 with 100, and 1000 , so the work grows with the size of list 
 n elements -> upto n elements shifted that's why we call it O(n) notation .
 
 whereas the number[2] does not require searching through the list .python directly access that location 
 so we call it O(1) notation, and this is the major DSA idea . 
 Big-O describe how the amount of work grows as the input get larger. 
"""

"""
 1 : O(1)- Constant time 
print(number[2])
 it does not check all element, just go to index given and result shows .
 Accessing a particular index is consider contant time. and this is O(1) and 1 does not mean
 one second one hour or some thing else. it means that work doesn't grow with the input size. 

 2: O(n) Linear time 
    Now consider number = [10,20,30,40,50]

    for number in numbers:
        print(number)
    if there aer 5 elements it requires 5 iteration, if 100 and if 1000.
    so the amount of work grows as the with n. Therefore  O(n)

    
3: Searching a list 
   consider numbers = [10, 20, 30, 40, 50]

   if 40 in number:
      print("found)

    python have to check one by one and if we are searching for something that isn't there ,
    python have to check all list condition is (if 100 in list) , check entire list .
    Therefore list memebership search is :  O(n)

Now O(n²)
This one look intimadating , but it's actually simple. 

number = [10,20,30,40,50]
for x in numbers:
   for y in numbers: 
      print(x, y)

for every iteration , the inner loop also run n time. so nxn = n²
therefore O(n²), for 5 elements 5*5=25 times 
That's why nested loops can become expensive very quickly. 

The Three you need to under stand 
Complexity          Basic Idea 
O(1)                work roughly stay constant.
O(n)                work grow with the number of elements
O(n²)               work grows with the square of the number of elements

"""