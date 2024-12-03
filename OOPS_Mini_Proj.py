class Library:
    def __init__(self, book_list, library_name):
        self.book_list = book_list
        self.library_name = library_name
        self.lend_record = {}

    def display_books(self):
        print("Books available in the library:")
        for book in self.book_list:
            print(book)

    def add_book(self):
        book = input("Enter Book Name: ")
        self.book_list.append(book)
        print(f"'{book}' has been added to the library.")

    def lend_book(self):
        book = input("Enter Book Name: ")
        if book not in self.book_list and book not in self.lend_record:
            print("Please enter a valid book name.")
        elif book in self.lend_record:
            print(f"The book '{book}' is already taken by {self.lend_record[book][0]}.")
        else:
            name = input("Enter Your Name: ")
            contact = input("Enter Your Contact No.: ")
            self.book_list.remove(book)
            self.lend_record[book] = (name, contact)
            print(f"'{book}' has been lent to {name}.")

    def return_book(self):
        book = input("Enter Book Name: ")
        if book in self.lend_record:
            self.book_list.append(book)
            del self.lend_record[book]
            print(f"'{book}' has been returned to the library.")
        else:
            print("Please enter a valid book name.")


if __name__ == '__main__':
    book_list = ['To Kill a Mockingbird', 'Don Quixote']
    nitin_library = Library(book_list, 'nitin_library')

    while True:
        user = input("\nD for Display Books, A for Add Books, L for Lend Books, R for Return Books, Q for Quit: ").upper()
        if user == 'Q':
            break
        elif user == 'D':
            nitin_library.display_books()
        elif user == 'A':
            nitin_library.add_book()
        elif user == 'L':
            nitin_library.lend_book()
        elif user == 'R':
            nitin_library.return_book()
        else:
            print("Please enter a valid input.\nD for Display Books, A for Add Books, L for Lend Books, R for Return Books, Q for Quit")
