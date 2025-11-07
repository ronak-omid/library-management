from book import Book
class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self,book):
        if isinstance(book,Book) and book not in self.book_list:
            self.book_list.append(book)
            return True
        return False

    def remove_book(self,book):
        if isinstance(book,Book) and book not in self.book_list:
            self.book_list.remove(book)
            return True
        return False
    
    def get_all_book_info(self):
        tex_to_show = ""
        for book in self.book_list:
            tex_to_show += str(book) + "\n"
        return tex_to_show
    
    def borrow(self,book):
        if isinstance(book,Book) and book in self.book_list:
            book.borrow()
    
    def return_book(self,book):
        if isinstance(book,Book) and book in self.book_list:
            book.return_book()

    def get_borrowed_book(self):
        text_to_show = ""
        for book in self.book_list:
            if book.is_borrowed:
                text_to_show += str(book) + "\n"
            return text_to_show
        
            
    def get_not_borrowed_book(self):
        text_to_show = ""
        for book in self.book_list:
            if not book.is_borrowed:
                text_to_show += str(book) + "\n"
            return text_to_show
    
    def get_author_books(self,author):
        return [book for book in  self.book_list if book.author.lower() == author.lower()]
    
    def search_by_title_or_author(self,search_text):
        return [ book for book in self.book_list if (book.author == search_text) or (book == search_text)]











        