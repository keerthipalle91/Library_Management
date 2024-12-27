Link:https://github.com/keerthipalle91/Library_Management/blob/main/mini%20projet-2.py
# Library Management System

A simple library management system implemented in Python. The system supports functionalities for both administrators and users, including book management, user management, and borrowing/returning books.

## Features

### Admin Features:
- Add new books to the library.
- Delete books from the library.
- Display all books in the library.
- View borrowed books and their details.

### User Features:
- Borrow books (up to a maximum limit).
- Return borrowed books and calculate fines for overdue returns.
- View a list of borrowed books with due dates.

## Requirements
- Python 3.6 or later

## How to Run

1. Clone the repository or download the code files.
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Run the `library_management_system.py` file.
   ```bash
   python library_management_system.py
   ```

## Predefined Users and Admin Credentials

### Admin Credentials:
- Username: `admin`
- Password: `admin123`

### Predefined Users:
| User ID  | Name       | Password       |
|----------|------------|----------------|
| `user1`  | Ravali     | `ravali123`    |
| `user2`  | Chandana   | `chandana456`  |

### Predefined Books:
| Book ID  | Title                     | Author          |
|----------|---------------------------|-----------------|
| `1`      | 1984                      | George Orwell   |
| `2`      | To Kill a Mockingbird     | Harper Lee      |

## Usage Instructions

### Admin Menu:
1. **Add Book**: Add a new book to the library by providing its title and author.
2. **Delete Book**: Remove a book from the library using its ID.
3. **Display All Books**: View all books in the library along with their availability status.
4. **Display Borrowed Books**: View a list of borrowed books, including borrower details and due dates.
5. **Logout**: Exit the admin menu.

### User Menu:
1. **Borrow Book**: Borrow a book by entering its ID. Each user can borrow up to 3 books at a time.
2. **Return Book**: Return a borrowed book by entering its ID. Fines are calculated at $1 per day for overdue books.
3. **Display Borrowed Books**: View a list of books currently borrowed by the user, along with their due dates.
4. **Logout**: Exit the user menu.

## Example Workflow

### Admin:
1. Login using the admin credentials.
2. Add a new book to the library.
3. Display the list of all books.
4. Logout.

### User:
1. Login using a predefined user ID and password.
2. Borrow a book using its ID.
3. View the list of borrowed books.
4. Return a book and check if a fine applies.
5. Logout.

## Code Structure

- **`Book` Class**: Represents a book in the library.
- **`User` Class**: Represents a library user with borrowing functionalities.
- **`Library` Class**: Manages books, users, and admin operations.

## Future Enhancements
- Add persistent storage for books and users.
- Implement a graphical user interface (GUI).
- Add email notifications for due dates and overdue books.
- Enhance security with encrypted passwords.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## Contact
For questions or feedback, feel free to contact the project maintainer.
