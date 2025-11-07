class Book :
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False
    
    def borrow(self):
        if self.is_brrowed:
            return f"{self.title} already borrowed."
        self.is_borrowed = True
        return f"book {self.title} borrowed!"
    
    def return_book(self):
        if not self.is_borrowed:
            return f"{self.title} already returned."
        self.is_borrowed = False
        return f"book {self.title} returned!"
    
    def __str__(self):
        return f"{self.title} written by {self.author} with {self.pages} pages"
    
    def __repr__(self):
        return f"{self.title} written by {self.author} with {self.pages} pages"
    
    def __eq__(self, o):
        if isinstance(o,Book):
            return self.title == o.title and self.author == o.author
        return self.title == o
        

    





    
    
    