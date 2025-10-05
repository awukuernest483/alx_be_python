class Book:
    def __init__(self, title, author, _is_checked_out):
      self.title = title
      self.author = author
      self._is_checked_out = _is_checked_out


class Library:
    def __init__(self, name, age):
      self.name = name
      self.age = age