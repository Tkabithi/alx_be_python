class Book:
    """Represents a book with a title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title  # public
        self.author = author  # public
        self._is_checked_out = False  # private by convention

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Manages a collection of Book objects."""

    def __init__(self):
        self._books = []  # private list of books

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title, if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Sorry, '{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"'{title}' was not checked out or does not exist.")

    def list_available_books(self):
        """Print all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")

