class Book:
    def __init__(self, __code, __title, __status=True):
        self.__code = __code
        self.__title = __title
        self.__status = __status

    def get_book_title(self):
        return self.__title

    def get_book_code(self):
        return self.__code

    def is_available(self):
        return self.__status

    def borrow_book(self):
        self.__status = False

    def return_book(self):
        self.__status = True

    def __str__(self):
        if self.__status:
            return f'{self.__title}, {self.__code} (Available)'
        else:
            return f'{self.__title}, {self.__code} (On Loan)'


class Member:
    def __init__(self, __member_id, __name, __on_loan_books_list=None):
        self.__member_id = __member_id
        self.__name = __name
        if __on_loan_books_list is None:
            self.__on_loan_books_list = []
        else:
            self.__on_loan_books_list = __on_loan_books_list

    def get_name(self):
        return self.__name

    def get_member_id(self):
        return self.__member_id

    def get_on_loan_books(self):
        return self.__on_loan_books_list

    def borrow_book(self, book):
        a = str(book)
        b = a[:a.index(",")]
        self.__on_loan_books_list += [b]

    def return_book(self, book):
        a = str(book)
        b = a[:a.index(",")]
        self.__on_loan_books_list.remove(b)

    def __str__(self):
        if self.__on_loan_books_list:
            a = ''
            for i in range(len(self.__on_loan_books_list)):
                if i != len(self.__on_loan_books_list) - 1:
                    a += str(self.__on_loan_books_list[i]) + "\n"
                else:
                    a += str(self.__on_loan_books_list[i])
            return f'{self.__name}\nOn loan book(s):\n{a}'
        else:
            return f'{self.__name}\nOn loan book(s):\n-'


class Record:
    def __init__(self, __book, __member, __issue_date=None):
        self.__book = __book
        self.__member = __member
        self.__is_on_loan = self.__book.is_available()
        if __issue_date is None:
            self.__issue_date = ''
        else:
            self.__issue_date = __issue_date
        self.__member.borrow_book(self.__book)
        self.__book.borrow_book()

    def get_member_id(self):
        return self.__member.get_member_id()

    def get_book_code(self):
        return self.__book.get_book_code()

    def get_issue_date(self):
        return self.__issue_date

    def is_on_loan(self):
        return self.__is_on_loan

    def return_book(self):
        self.__book.return_book()
        self.__member.return_book(self.__book)

    def __str__(self):
        return f'{str(self.__member.get_name())}, {str(self.__book)}, issued date={self.__issue_date}'

    def get_book_title(self):
        return self.__book.get_book_title()

    def get_member_name(self):
        return self.__member.get_name()

    def get_book_status(self):
        return self.__book.is_available()


class MyLibrary:
    def __init__(self, simple_books):
        self.__on_loan_records_list = []
        try:
            with open(str(simple_books), 'r') as txt:
                return1 = []
                while txt.read != "":
                    txt.read = txt.readline()

                    if txt.read != "":
                        if txt.read[-1] == "\n":
                            return1 += [txt.read[:-1]]
                        else:
                            return1 += [txt.read[:]]
                return3 = []
                for i in range(len(return1)):
                    return2 = []
                    a = return1[i]
                    index1 = a.index(',')
                    book__title = a[:index1]
                    book__code = a[index1 + 1:]
                    return2 += [book__title]
                    return2 += [book__code]
                    return3 += [Book(return2[0], return2[1])]

                self.__books_list = return3
                print(f"{len(self.__books_list)} books loaded.")
        except:
            print(f"ERROR: The file '{simple_books}' does not exist.")

    def show_all_books(self):
        try:
            for i in range(len(self.__books_list)):
                if i != len(self.__books_list) - 1:
                    print(str(self.__books_list[i]))
                else:
                    print(str(self.__books_list[i]))
        except AttributeError:
            pass

    def find_book(self, code):
        for i in range(len(self.__books_list)):
            if code == self.__books_list[i].get_book_code() and self.__books_list[i].is_available():
                return self.__books_list[i]

        return None

    def borrow_book(self, book, member, issue_date):
        if book == None:
            print("ERROR: could not issue the book.")
        else:
            re1 = Record(book, member, issue_date)
            self.__on_loan_records_list += [re1]
            print(f"{re1.get_book_title()} is borrowed by {re1.get_member_name()}.")

    def show_available_books(self):
        for i in range(len(self.__books_list)):
            if self.__books_list[i].is_available():
                print(self.__books_list[i])

    def find_record(self, code):
        for i in range(len(self.__on_loan_records_list)):
            if self.__on_loan_records_list[i].get_book_code() == code and self.__on_loan_records_list[i].is_on_loan():
                return self.__on_loan_records_list[i]
        return None

    def return_book(self, record):
        if record != None:
            if not record.get_book_status():
                record.return_book()
                print(f"{record.get_book_code()} is returned successfully.")
            else:
                print("ERROR: could not return the book.")
        else:
            print("ERROR: could not return the book.")

    def show_on_loan_records(self):
        for i in range(len(self.__on_loan_records_list)):
            if not self.__on_loan_records_list[i].get_book_status():
                print(self.__on_loan_records_list[i])
            else:
                pass

    def show_all_records(self):
        for i in range(len(self.__on_loan_records_list)):
            print(self.__on_loan_records_list[i])
