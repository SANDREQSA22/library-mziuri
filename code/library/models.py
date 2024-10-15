


#to easy     copy paste from old homework  :))))



class Librarian:
    def __init__(self, name, surname, email, salary):
        self.name = name
        self.surname = surname
        self.email = email
        self.salary = salary

    def __str__(self):
        return f"Librarian: {self.name} {self.surname}, Email: {self.email}, Salary: {self.salary}"




class User:
    def __init__(self, name, surname, email, active=True):
        self.name = name
        self.surname = surname
        self.email = email
        self.active = active  
        self.taken_book = None  

    def checkout_book(self, book):
        if book.is_taken:
            return False  
        if self.taken_book is None:
            self.taken_book = book
            book.is_taken = True
            return True
        else:
            return False  

    def return_book(self):
        if self.taken_book is not None:
            self.taken_book.is_taken = False
            self.taken_book = None
            return True
        return False

    def __str__(self):
        return f"User: {self.name} {self.surname}, Email: {self.email}, Active: {self.active}"



class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Category: {self.name}"


class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.is_taken = False

    def __str__(self):
        return f"Book: {self.title} by {self.author}, Category: {self.category}, Taken: {self.is_taken}"
