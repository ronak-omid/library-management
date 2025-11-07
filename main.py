from book import Book
from Library import Library
lib = Library()

menu = """
===== Library Management System =====
1) Add a book 
2) Remove a book
3) show number of borrowed books
4) Show total number of books
5) Show number of available books
6) Searsh by title or author
7) Borrow a book
8) Return a book
9) Show books by an author
10) Show all books
0) Exit
===============================================
"""

while True:
    print(menu)
    choice = input("Your choice: ").strip()

    if choice == "1":
        title = input("Title: ").lower()
        author = input("Author: ").lower()
        pages_s = input("Pages: ").lower()

        pages = int(pages_s)

        book = Book(title,author,pages)
        added = False
        if lib.add_book(book):
            added = True
        else:
            added = False

        print("Book added" if added else "Book not added(maybe duplicate).")
    elif choice == "2":
        search_text = input("(title or author) to find books to remove: ").lower()
        res = lib.search_by_title_or_author(search_text)
        
        print("select book: ")
        for index, book in enumerate(res):
            print(f"{index}. {book}")
        
        index = int(input("index: "))
        book = res[index]
        removed = lib.remove_book(book)
        print("Removed." if removed else "Remove failed.")

    elif choice == "3":
        print(lib.get_borrowed_book())
    
    elif choice == "4":
        print(lib.get_all_book_info)
    
    elif choice == "5":
        print(lib.get_not_borrowed_book)
    
    elif choice == "6":
        search_text =  input("(title or author) to find books: ").lower()
        res = lib.search_by_title_or_author(search_text)
        print(res)
    
    elif choice == "7":
        search_text = input("(title or author) to find books to borrow: ").lower()
        res = lib.search_by_title_or_author(search_text)

        print("select book: ")
        for index, book in enumerate(res):
            print(f"{index}. {book}")
        
        index = int(input("index: "))
        book = res[index]
        borrow = lib.borrow(book)
        print(borrow)

    elif choice == "8":
        search_text =  input("(title or author) to find books: ").lower()
        res = lib.search_by_title_or_author(search_text)

        print("select book: ")
        for index, book in enumerate(res):
            print(f"{index}. {book}")
        
        index = int(input("index: "))
        book = res[index]
        returned = lib.return_book(book)
        print(returned)

    elif choice == "9":
        author = input("author name: ")
        print(lib.get_author_books(author))
    
    elif choice == "10":
        print(lib.get_all_book_info)
    
    elif choice == "0":
        print("Goodbye")
        break
    else:
        print("invalid option. please try again.")




    


