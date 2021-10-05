import os
import time


class Library:

    def __init__(self, NameOfLib):
        self.name = NameOfLib
        k = os.path.join(self.name)
        if not os.path.exists(k):
            os.mkdir(self.name)
        with open(self.BooksAddress,"a") as f:
            pass
        with open(self.DonationAddress,"a") as f:
            pass
        with open(self.IssueLogAddress,"a") as f:
            pass
        with open(self.MembersRegAddress,"a") as f:
            pass


    def AddBook(self, bookName, Availablity="A"):
        with open(self.BooksAddress, "a") as f:
            bookId = input("Enter a unique bookId")
            if self.BookIds.__contains__(bookId):
                print("Enter Diiferent one This Is available")
                self.AddBook(bookName)
            elif len(bookId)>10:
                print("Enter id within 10 Characters")
                self.AddBook(bookName)

            else:
                f.write(f"{bookId}@{bookName}@{Availablity}\n")

    def DonateBook(self):
        Donar = input("Enter the name of Donar :")
        bookName = input("Enter the name of Book donated")
        with open(self.DonationAddress, "a") as f:
            t = time.asctime(time.localtime(time.time()))
            f.write(f"{bookName}@{Donar}@{t}")
            self.AddBook(bookName)

    def BookListGenerator(self):
        with open(self.BooksAddress, "r") as f:
            for book in f:
                temp = book.split("@")
                yield temp

    def printBooks(self):
        t = self.BookListGenerator()
        for k in t:
            print(k[1])

    def getAList(self, intOfReq):
        """0 -for ids
           1 -for books
           2 -for Availability"""
        l = []
        i = 0
        gen = self.BookListGenerator()
        for k in gen:
            l.append(k[intOfReq])
        return l

    def ReprintLists(self, Address, listToPrint):
        with open(Address, "w") as F:
            for line in listToPrint:
                F.write(line)

    def writeBookList(self, ids, names, avail):
        l = list(map(lambda x, y, z: f"{x}@{y}@{z}", ids, names, avail))
        self.ReprintLists(self.BooksAddress, l)

    def SetBookStatus(self, bookId, isAvailable):
        isA = "A" if isAvailable else "N"
        ids = self.BookIds
        stat = self.BookAvList
        st = "Invalid Id"
        isDone = False
        for id in ids:
            if id.__eq__(str(bookId)):
                stat[ids.index(id)] = f"{isA}\n"
                st = "Done"
                isDone = True
        print(st)
        self.writeBookList(ids, self.Books, stat)
        return isDone

    def CheckAvailablity(self, bookId):
        bo = False
        if self.BookIds.__contains__(str(bookId)):
            stat = self.BookAvList[self.BookIds.index(bookId)]
            if stat.__eq__("A\n"):
                bo = True
        return bo

    def MembersList(self):
        s = ""
        with open(self.MembersRegAddress) as f:
            for Lines in f:
                s = s + Lines

        l = s.split("\n")
        return l

    def AddMember(self):
        Memberid = str(input("Enter An unique Id :"))
        if self.MembersList().__contains__(Memberid):
            print("This Id has been taken")
            self.AddMember()
        elif Memberid.__contains__("@"):
            print("You cant Include '@'")
            self.AddMember()
        elif len(Memberid)>10:
            print("Enter id within 10 Characters")

            self.AddMember()
        else:
            with open(self.MembersRegAddress, "a") as f:
                f.write(f"{Memberid}\n")

    def listofbookstakenbyPerson(self, IdOfPerson):
        l = []
        with open(tanu.IssueLogAddress) as f:
            for Line in f:
                if Line.__contains__(f"@{IdOfPerson}@"):
                    l.append(Line)
        return l

    def LogOfBook(self, BookId):
        l = []
        with open(tanu.IssueLogAddress) as f:
            for Line in f:
                if Line.startswith(f"{BookId}@"):
                    l.append(Line)
        if len(l) > 0:
            l1 = list(map(lambda x: "   ".join(str(x).split("@")),l))
            for k in l1:
                print(k)


    def currentBook(self, IdOfPerson):
        l = self.listofbookstakenbyPerson(IdOfPerson)
        book = "None"

        if len(l) > 0:
            k=len(l)
            v = str(l[k-1])
            book = v.split("@")[0] if v.__contains__("@Issued@") else "None"

        return book

    def IssueOrReturnBook(self, IorR):
        IdofPerson = input("Enter the id of a person :")
        BookId = input("Enter the id of a Book :")
        if self.currentBook(IdofPerson).__eq__("None"):
            if str(IorR).__eq__("I"):
                self.BookStatus(IdofPerson, BookId, IorR)
            else:
                print("You Dont have book acc to Our Database")
        else:
            if str(IorR).__eq__("R"):
                if self.currentBook(IdofPerson).__eq__(BookId):
                    self.BookStatus(IdofPerson, BookId, IorR)
                else:
                    print("I guess U have Entered wrong book id. plz Enter the ccorrect one")
            else:
                print(f"You have already have a book with id:{self.currentBook(IdofPerson)}",
                      "Return that first")



    def BookStatus(self, IdOfAPerson, Bookid, IorR):
        stat = True if str(IorR).__eq__("I") else False
        if self.MembersList().__contains__(IdOfAPerson):
            with open(self.IssueLogAddress, "a") as f:
                t = time.asctime(time.localtime(time.time()))
                if self.CheckAvailablity(Bookid) and stat:
                    if self.SetBookStatus(Bookid, False):
                        f.write(f"{Bookid}@{IdOfAPerson}@Issued@{t}\n")
                        print("Issue successful")
                elif (not self.CheckAvailablity(Bookid)) and not stat:
                    if self.SetBookStatus(Bookid, True):
                        f.write(f"{Bookid}@{IdOfAPerson}@Returned@{t}\n")
                        print("Returned")
                else:
                    if stat:
                        print("You Cant Issue the book as it is not available .",
                              "Please choose another")
                    else:
                        print("This book is not borrowed yet.plz check your bookid again")
        else:
            print("You Are not a member . plz signup for member first")

    @property
    def BooksAddress(self):
        add = os.path.join(self.name, "Books.txt")
        return add

    @property
    def IssueLogAddress(self):
        add = os.path.join(self.name, "Log.txt")
        return add

    @property
    def MembersRegAddress(self):
        add = os.path.join(self.name, "MemberListLog.txt")
        return add

    @property
    def DonationAddress(self):
        add = os.path.join(self.name, "BorrowLog.txt")
        return add

    @property
    def BookIds(self):
        return self.getAList(0)

    @property
    def Books(self):
        return self.getAList(1)

    @property
    def BookAvList(self):
        return self.getAList(2)


tanu = Library("Tanmai")
while True:
    print("1:Add new member\n",
          "2:Issue a book\n",
          "3:Return a Book\n",
          "4:Donate a Book\n",
          "5:Get Log of a Book\n",
          "6 : Get log of a Member\n",
          "7:Add a book\n",
          "8:Donation Log\n",
          "9:Check Current book\n",
          "10: Check Available Books\n",
          "11:Chech status of All Members\n",
          "12: Quit\n")
    try:
        i = int(input("Your Choice:  "))
    except:
        print("Error")
        continue
    if i == 1:
        tanu.AddMember()
    elif i == 2:
        tanu.IssueOrReturnBook("I")
    elif i == 3:
        tanu.IssueOrReturnBook("R")
    elif i == 4:
        tanu.DonateBook()
    elif i == 5:
        id = str(input("Enter BookId:"))
        tanu.LogOfBook(id)
    elif i==6:
        id = str(input("Enter ur Id:"))

        l = tanu.listofbookstakenbyPerson(id)
        l1=list(map(lambda x:"    ".join(str(x).split("@")),l))
        if len(l1)>0:
            print("Bookid    Member    Process    Time\n")
            for i in l1:
                print(i)
        else:
            print("No Log yet")
    elif i==7:
        id = str(input("Enter the Name of the Book :\n"))
        tanu.AddBook(id)
    elif i==8:
        tanu.DonateBook()
    elif i==9:
        id = str(input("Enter ur Id:"))
        book=tanu.currentBook(id)
        print(f"Book status :{book}")
    elif i==10:
        print("Available Books :")
        print(f"BookId"," "*10,"Name of Book\n")
        l=filter(lambda x:tanu.CheckAvailablity(x),tanu.BookIds)
        for ids in l:
            k=(18-len(str(ids)))*" "
            print(f"{ids}{k}{tanu.Books[tanu.BookIds.index(ids)]}")
    elif i==12:
        break
    elif i==11:
        for ids in tanu.MembersList():
            k=(15-len(ids))*" "
            print(f"{ids}{k}:{tanu.currentBook(ids)}")
    print("Done\n","**********************************")
    time.sleep(3)
