class Book:
    
    
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity



    def display_info(self):
        print("*"*20)
        print("Title : ", self.title)
        print("Book ID :", self.book_id)
        print("Author :", self.author)
        print("Quantity  :", self.quantity)   


    def  borrow_book(self):
        print("Book", self.title)
        self.quantity -= 1


    def return_book(self):
        print("Book ", self.title)
        self.quantity += 1


class Library():
    def __init__(self):
        self.books = []
        for book in self.books:
            book.dislay_info()
        
    def add_book(self, book):
         self.books.append(book)


    def display_books(self):
        for book in self.books:
            book.display_info()

python_book = Book(101, "Python", "Eric", 5)
sql_book = Book(102, "SQL", "John", 4)
data_book = Book(103, "Data Engineering", "JS Thomson", 3)

library = Library()

library.add_book(python_book)
library.add_book(sql_book)
library.add_book(data_book)

library.display_books()






 
  
    
