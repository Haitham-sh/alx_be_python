class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = [
            Book("check_out_book", "Aldous Huxley"),
            Book("1984", "George Orwell"),
            
        ]

        def return_book(self):
            pass

        

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def check_out(self, book):
        """Check out a book from the library."""
        if book in self.books and not book._is_checked_out:
            book._is_checked_out = True
            return True
        return False

    def return_book(self, book):
        """Return a checked-out book to the library."""
        if book in self.books and book._is_checked_out:
            book._is_checked_out = False
            return True
        return False

    def list_books(self):
        """List all books in the library."""
        return [book.title for book in self.books]
    