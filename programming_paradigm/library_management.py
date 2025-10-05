class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def __str__(self):
        """method that defines how an object should be represented as a string"""
        return f"{self.title} by {self.author}"
    def check_out(self):
        self._is_checked_out = True
    def return_book(self):
        self._is_checked_out = False
    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
       """Adding a new book""" 
       self._books.append(book)
    def check_out_book(self,title):
        for book in self._books:
            if book.title == title: 
                if book.is_available():
                    book.check_out()
                    return
                else:
                    print(f"'{title}' is already checked out.")
        print(f"'{title}' not found in the library.")

    def return_book(self,title):
        for book in self._books:
            if book.title == title :
                book.return_book()
                return
        print(f"'{title}' does not exist.")
    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(book)



    

