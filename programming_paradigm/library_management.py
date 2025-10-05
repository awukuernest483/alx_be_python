class Book:
    def __init__(self, title, author, _is_checked_out=False):
      self.title = title
      self.author = author
      self._is_checked_out = _is_checked_out
      
    


class Library:
    def __init__(self):
        self.books = []
        
        
    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")
        
        
    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Checked out: {book.title}")
                return
            print(f"Book titled '{title}' not found.")
        
            
    def return_book(self, book):
        self.books.append(book)
        return True
    
            
    def list_available_books(self):
        print (self.books)
        
            
        