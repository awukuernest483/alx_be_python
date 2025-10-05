class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out

    def __repr__(self):
        return f"<Book: {self.title} by {self.author}>"

class Library:
    def __init__(self):
        self.books = []
        self.checked_out_books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                self.checked_out_books.append(book)
                print(f"Checked out: {book.title}")
                return True
        print(f"Book titled '{title}' not found.")
        return False

    # 👇🏾 This is the return_book method your main.py is expecting
    def return_book(self, title):
        for book in self.checked_out_books:
            if book.title == title:
                self.checked_out_books.remove(book)
                self.books.append(book)
                print(f"Returned: {book.title}")
                return True
        print(f"Book titled '{title}' not found in checked-out books.")
        return False

    def list_available_books(self):
        print("Available books:")
        print(self.books)
