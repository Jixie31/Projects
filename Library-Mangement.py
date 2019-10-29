class Library:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lendDict = {}           

    def Displyabook(self):
        print(f"We have following books in a library: {self.library_name}")
        for book in self.list_of_books:
            print(book)

    def lendbook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender-book database has been updated. you can take the book now")
        else:
            print(f"book is already being used by {self.lendDict[book]}")

    def addbook(self, book):
        self.list_of_books.append(book)
        print("book has been added to the book list")

    def returnbook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    jixie = Library(['python', 'rich dad poor dad', 'harry potter', 'c++ basics', 'algorithm by CLRS'], "codejixie")    

    while(True):
        print(f"Welcome to the {jixie.library_name} library. Enter your choice")
        print(("1. Display Book"))
        print(("2. Lend Book"))
        print(("3. Add a Book"))
        print(("4. Return a Book"))
        user_choice = (input())

        if user_choice not in ['1','2','3','4']:
            print("enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            jixie.Displyabook()

        elif user_choice ==2:
            book = input("enter the name of the book")
            user = input("enter your name")
            jixie.lendbook(user, book)

        elif user_choice == 3:
            book = input("enter the name of book you want to add:")
            jixie.addbook(book)

        elif user_choice ==4:
            book = input("enter the name of book you want to return:")
            jixie.returnbook(book)
            print("Thank you for returning the book")

        else:
            print("Not a valid option")

        print("press q to quit and c to continue")
        user_choice2 = ""
        
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()

            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue

