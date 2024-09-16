class Library:
    def __init__(self, name, booklist):
        self.booklist = booklist  # List of available books
        self.name = name  # Name of the library
        self.lendDict = {}  # Dictionary to track which user has borrowed which book

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict[book] = user  # Add the book and the user to the lend dictionary
            print("Lender-Book Database has been updated. You can take the book now.")
        else:
            print(f"Sorry, the book is already in use by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the library.")

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            print(f"The book '{book}' has been returned.")
        else:
            print("This book was not lent out from this library.")

if __name__ == "__main__":
    a = Library("Central Library", ["Python", "C++", "C", "Java", "Machine Learning"])

    while True:
        print(f"\nWelcome to the {a.name}. Enter your choice to continue:")
        print("1. Display books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        choice = input()

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid input, please try again.")
            continue
        else:
            choice = int(choice)

        if choice == 1:
            a.displayBooks()

        elif choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            a.lendBook(user, book)

        elif choice == 3:
            book = input("Enter the name of the book you want to add: ")
            a.addBook(book)

        elif choice == 4:
            book = input("Enter the name of the book you want to return: ")
            a.returnBook(book)

        print("\nPress 'q' to quit or 'c' to continue")
        choice2 = ""
        while choice2 not in ["c", "q"]:
            choice2 = input().lower()
            if choice2 == "q":
                exit()
            elif choice2 == "c":
                break

            


            

            
        
        
          
