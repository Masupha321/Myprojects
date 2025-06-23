class Book:
    def __init__(self, book_title, author, book_id):
        self.book_title = book_title
        self.author = author
        self.book_id = book_id
        self.is_available = True
    
    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_book(self):
        self.is_available = True

    def display_details(self):
       status = "Available" if self.is_available else "Borrowed"
       print("Book ID: {self.book_id} | Title: {self.book_title} | Author: {self.author} | Status: {status}")

class Member:
    def __init__(self, member_name, member_id):
        self.member_name = member_name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow (self, book_id):
        self.borrowed_books.append(book_id)

    def borrow (self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
    
    def display_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.member_name} has not borrowed any books.")
        else:
            print(f"{self.member_name} borrowed books: {', '.join(map(str, self.borrowed_books))}")

class Library:
    def __init__(self, name="IM Library"):
         self.name = name
         self.books = {}
         self.members = {}
    
    def add_book(self, book_title, author, book_id):
        if book_id in self.books:
            print("Book ID already exists.")
            return
        self.books[book_id] = Book(book_title, author, book_id)
        print("Book added successfully.")

    def register_member(self, member_name, member_id):
        if member_id in self.members:
            print("Member ID already exists.")
            return
        self.members[member_id] = Member(member_name, member_id)
        print(f"Member '{member_name}' registered successfully.")

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Invalid member ID.")
            return
        if book_id not in self.members:
            print("Invalid member ID.")
        if book_id not in self.books:
            print("Invalid book ID.")
            return
        if self.books[book_id].borrow():
            self.members[member_id].borrow(book_id)
            print(f"Book '{self.books[book_id].book_title}' borrowed succesfully.")
        else:
            print("Book is currently unavailable.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Invalid member ID.")
            return
        if book_id not in self.books:
            print("Invalid book ID.")
            return
        if book_id in self.members[member_id].borrowed_books:
            self.members[member_id].return_book(book_id)
            self.books[book_id].return_book()
            print(f"Book '{self.books[book_id].book_title}' returned succesfully.")
        else:
            print("Member has not borrowed this book.")

    def display_all_books(self):
            if not  self.books:
                print("No books in the library.")
            else:
                for book in self.books.values():
                    book.display_details()

    def display_members(self):
            if not self.members:
                print("No members registered.")
            else:
                for member in self.members.values():
                    print(f"Member ID: {member.member_id} | Name: {member.member_name}")

    def main():
        library = Library()

        while True:
            print(f"\nWelcome to {library.name}!")
            print("1. Add Book")
            print("2. Register Member")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Display All Books")
            print("6. Display Members")
            print("7. Check Availabilty of a Book")
            print("8. Exit")

            choice = input("Enter your choice:")

            if choice == "1":
                book_title = input("Enter book title: ")
                author = input("Enter author name: ")
                book_id = int(input("Enter book ID: "))
                library.add_book(book_title, author, book_id)

            elif choice == "2":
                member_name = input("Enter member name: ")
                member_id = int(input("Enter member ID: "))
                library.register_member(member_name, member_id)
            
            elif choice == "3":
                member_id = int(input("Enter member ID: "))
                book_id = int(input("Enter book ID: "))
                library.borrow_book(member_id, book_id)

            elif choice == "4":
                member_id = int(input("Enter member ID: "))
                book_id = int(input("Enter book ID: "))
                library.return_book(member_id, book_id)

            elif choice == "5":
                library.display_all_books()
            
            elif choice == "6":
                library.display_members()

            elif choice == "7":
                book_id = int(input("Enter book ID to check availabilty: "))
                if book_id in library.books:
                    library.books[book_id].display_details()

            elif choice == "8":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

Library.main() # function call to start the program.
