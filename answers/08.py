
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def get_description(self):
        return f"{self.title} by {self.author}, Pages: {self.pages}"


new_book = Book("Wuthering Heights", "Emily Bronte", 432)
print(new_book.get_description())