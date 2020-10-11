class Library(object):
    """docstring for Library."""

    def __init__(self):
        super(Library, self).__init__()
        self.books = ["Who moved my cheese", "100 days of solitude", "1984"]
        self.borrowedBooks = []

    def listAvailableBooks(self):
        for book in self.books:
            print(book)

    def borrowBook(self, book):
        if book not in self.books:
            print("Sorry, {} not available".format(book))
        else:
            self.borrowedBooks.append(book)
            index = self.books.index(book)
            del self.books[index]

    def returnBook(self, book):
        if book not in self.borrowedBooks:
            print("Sorry, the book {} was not borrowed from this library".
                  format(book))
        else:
            index = self.borrowedBooks.index(book)
            del self.borrowedBooks[index]
            self.books.append(book)


mylibrary = Library()
mylibrary.listAvailableBooks()
mylibrary.borrowBook("7 habits of highly efficient people")
print("Borrowing a Book")
mylibrary.borrowBook("1984")
mylibrary.listAvailableBooks()
print("Return book")
mylibrary.returnBook("1984")
mylibrary.listAvailableBooks()
