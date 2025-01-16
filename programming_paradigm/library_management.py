class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        """
        Initialize the book with a title, author, and its availability status.
        :param title: The title of the book.
        :param author: The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if self._is_checked_out:
            return False  # The book is already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned."""
        if not self._is_checked_out:
            return False  # The book was not checked out
        self._is_checked_out = False
        return True

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """A class to manage a collection of books."""

    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []

    def add_book(self, book):
        """
        Add a book to the library.
        :param book: An instance of the Book class.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by its title.
        :param title: The title of the book to check out.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """
        Return a book by its title.
        :param title: The title of the book to return.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
