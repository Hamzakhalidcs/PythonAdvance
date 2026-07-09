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


    def borrow_book(self):
        print("Book", self.title)
        self.quantity -= 1


    def return_book(self):
        print("Book ", self.title)
        self.quantity += 1


class Library(Book):
    def __init__(self):
        self.books = []
        for book in self.books:
            book.dislay_info()
        
    def add_book(self, book):
         self.books.append(book)


    def display_book(self):

        for book in self.books:
            print(book.display_info())

        if not self.books:
            print("No Books in the Library")

   
    def search_book(self, title):
        """Return the book object if found, else None."""

        search_title = title.lower()
        
        for book in self.books:
            if book.title.lower() == search_title:
                book.display_info()
                return book  # ← Returns the book object
            
        return None  # ← Returns None if not found

    
    def borrow_book(self, title):
        """Borrow a book if exist and is available"""

        book = self.search_book(title)

        if not book:
            print(f" Book {title} not found in Library")
            return False
        
        if book.quantity<=0:
            print(f"'{book.title}' is Currently Unavailable (0 Coopies Left)")
            return False
        
        book.borrow_book()
        print(f"Successfully Borrowed '{book.title}' Book.")
        




python_book = Book(101, "Python", "Eric", 5)
sql_book = Book(102, "SQL", "John", 4)
data_book = Book(103, "Data Engineering", "JS Thomson", 3)

library = Library()

library.add_book(python_book)
library.add_book(sql_book)
library.add_book(data_book)

# library.display_book()
# library.search_book('ISLAMIAT')
# another_book = python_book
# print(another_book is python_book)

library.borrow_book("Python")
library.search_book('Python')



 
  
    
