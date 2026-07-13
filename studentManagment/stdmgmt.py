class BookUnavailableError(Exception):
    """Raised when trying to borrow a book that has no copies available."""
    pass

class BookNotFoundError(Exception):
    """Raised when trying to borrow a book that doesn't exist in the library."""
    pass

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
        self.quantity -= 1


    def return_book(self):
        self.quantity += 1

 

class Library():
    def __init__(self):
        self.books = []

        
    def add_book(self, book):
         self.books.append(book)


    def display_book(self):

        for book in self.books:
            (book.display_info())

        if not self.books:
            print("No Books in the Library")
    
    def search_book(self, title):
        """Return the book object if found, else None."""

        search_title = title.lower()
        
        for book in self.books:
            if book.title.lower() == search_title:
                return book
                # book.display_info() #in case you need to display the book info when found 
                # return book  # ← Returns the book object
            
        return None  # ← Returns None if not found
    
    def find_book(self, title):
        """Return the book object if found, else None."""
        
        book = self.search_book(title)
        if book:
            print(f"Book {title} Found in Library")
            book.display_info()
            return book
        
        else:
            print(f"Book {title} not Found in Library")
            return None


    def check_quantity(self, title): 
        book = self.search_book(title)
        if book:
            print(f"Book {title} has {book.quantity} Copies Left")
            return book.quantity
        
        else:
            print(f"Book {title} not Found")
            return None
    
    def borrow_book(self, title):
        """Borrow a book if exist and is available"""

        book = self.search_book(title)

        if not book:
            # print(f"Book {title} not found in Library")
            raise BookNotFoundError(f"Book {title} not found in Library")
            # return False    
        
        if book.quantity<=0:
            print(f"'{book.title}' is Currently Unavailable (0 Coopies Left)")
            return False
        
        book.borrow_book()
        print(f"Successfully Borrowed '{book.title}' Book.")
        
    def return_book(self, title):
        """Return a book if exist in the library"""

        book = self.search_book(title)

        if not book:
            print(f"Book {title} not found in Library")
            return False
        
        book.return_book()
        print(f"Successfully Returned '{book.title}' Book.") 




python_book = Book(101, "Python", "Eric", 5)
sql_book = Book(102, "SQL", "John", 4)
data_book = Book(103, "Data Engineering", "JS Thomson", 3)

library = Library()

library.add_book(python_book)
library.add_book(sql_book)
library.add_book(data_book)

# library.display_book()
# another_book = python_book
# print(another_book is python_book)


library.borrow_book("Python")

print("*"*30)
library.check_quantity('Python')

print("*"*30)

library.return_book("Python")
print("*"*30)
library.check_quantity('Python')

print("*"*30)
library.find_book("python")

 
  
    
