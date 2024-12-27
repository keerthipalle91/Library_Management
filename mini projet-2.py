from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.borrowed_by = None
        self.due_date = None

    def __str__(self):
        return f"{self.title} by {self.author}"

class User:
    def __init__(self, user_id, name, password, max_books=3):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.borrowed_books = {}
        self.max_books = max_books

    def borrow_book(self, book, borrow_date):
        if len(self.borrowed_books) >= self.max_books:
            print(f"Sorry, {self.name} cannot borrow more than {self.max_books} books.")
            return
        if book.is_available:
            book.is_available = False
            book.borrowed_by = self
            book.due_date = borrow_date + timedelta(days=7)
            self.borrowed_books[book.book_id] = book
            print(f"{self.name} borrowed {book.title}. Due date: {book.due_date.date()}")
        else:
            print(f"Sorry, {book.title} is currently not available.")

    def return_book(self, book, return_date):
        if book.book_id in self.borrowed_books:
            overdue_days = (return_date - book.due_date).days
            fine = max(0, overdue_days) * 1  # $1 per day fine for late return
            self.borrowed_books.pop(book.book_id)
            book.is_available = True
            book.borrowed_by = None
            book.due_date = None
            print(f"{self.name} returned {book.title}. Fine: ${fine}")
        else:
            print(f"{self.name} did not borrow {book.title}.")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books.values():
                print(f"- {book.title} (Due Date: {book.due_date.date()})")
        else:
            print(f"{self.name} has not borrowed any books.")

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.admins = {"admin": "admin123"}  # Admin credentials

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added to the library.")

    def delete_book(self, book_id):
        if book_id in self.books:
            deleted_book = self.books.pop(book_id)
            print(f"Book '{deleted_book.title}' has been deleted from the library.")
        else:
            print("Book not found in the library.")

    def add_user(self, user):
        self.users[user.user_id] = user
        print(f"User '{user.name}' added to the library system.")

    def display_all_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(f"- {book.title} by {book.author} (Available: {'Yes' if book.is_available else 'No'})")
        else:
            print("No books in the library.")

    def display_borrowed_books(self):
        print("Borrowed Books:")
        for book in self.books.values():
            if not book.is_available:
                print(f"- {book.title} by {book.author} (Borrowed by: {book.borrowed_by.name}, Due: {book.due_date.date()})")

def get_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Main program
if __name__ == "__main__":
    library = Library()

    # Predefined users
    library.add_user(User("user1", "ravali", "ravali123"))
    library.add_user(User("user2", "chandana", "chandana456"))

    # Predefined books
    library.add_book(Book(1, "1984", "George Orwell"))
    library.add_book(Book(2, "To Kill a Mockingbird", "Harper Lee"))

    while True:
        print("\nLibrary System:")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter admin username: ").strip()
            password = input("Enter admin password: ").strip()

            if username in library.admins and library.admins[username] == password:
                print("Welcome, Admin!")
                while True:
                    print("\nAdmin Menu:")
                    print("1. Add Book")
                    print("2. Delete Book")
                    print("3. Display All Books")
                    print("4. Display Borrowed Books")
                    print("5. Logout")

                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        title = input("Enter book title: ")
                        author = input("Enter book author: ")
                        book_id = len(library.books) + 1
                        library.add_book(Book(book_id, title, author))

                    elif admin_choice == "2":
                        book_id = int(input("Enter book ID to delete: "))
                        library.delete_book(book_id)

                    elif admin_choice == "3":
                        library.display_all_books()

                    elif admin_choice == "4":
                        library.display_borrowed_books()

                    elif admin_choice == "5":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Invalid admin credentials.")

        elif choice == "2":
            user_id = input("Enter your user ID: ").strip()
            password = input("Enter your password: ").strip()

            if user_id in library.users and library.users[user_id].password == password:
                user = library.users[user_id]
                print(f"Welcome, {user.name}!")
                while True:
                    print("\nUser Menu:")
                    print("1. Borrow Book")
                    print("2. Return Book")
                    print("3. Display Borrowed Books")
                    print("4. Logout")

                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        book_id = int(input("Enter book ID to borrow: "))
                        if book_id in library.books:
                            borrow_date = datetime.now()
                            user.borrow_book(library.books[book_id], borrow_date)
                        else:
                            print("Book not found.")

                    elif user_choice == "2":
                        book_id = int(input("Enter book ID to return: "))
                        if book_id in library.books:
                            return_date = datetime.now()
                            user.return_book(library.books[book_id], return_date)
                        else:
                            print("Book not found.")

                    elif user_choice == "3":
                        user.display_borrowed_books()

                    elif user_choice == "4":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Invalid user ID or password.")

        elif choice == "3":
            print("Exiting the system...")
            break

        else:
            print("Invalid choice. Please try again.")
