class Library:
    def __init__ (self,list,name):
     self.bookslist= list
     self.name=name
     self.lendDict={}

    def displayBooks(self):
        print(f"We have following books in our Library: {self.name}")
        for book in self.bookslist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book Database has been updated.you can take the book now")
        else:
            print(f"Book is already in use by {self.lendDict[book]}")

    def addBook(self,book):
        self.bookslist.append(book)
        print("Book has been added to your list")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    manas = Library (['Python','C++','Java','MachineLearning'], "CodeWithManas")

    while (True):
        print(f"welcome to the {manas.name}library.Enter your choice to continue")
        print("1.Display books")
        print("2.Lend book")
        print("3.Add book")
        print("4.Return book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            manas.displayBooks()

        elif user_choice == 2:
            book=input("Enter the name of the book you want to lend :")
            user=input("Enter Your Name :")
            manas.lendBook(user,book)

        elif user_choice == 3:
            book=input("Enter the name of the book you want to add :")
            manas.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return :")
            manas.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice == "q":
                break
            elif user_choice == "c":
                continue

            
