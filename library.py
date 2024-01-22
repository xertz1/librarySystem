# CS1026a 2023
# Assignment 2 - Library
# Kishore Piratheepan


# Description of Project:
# The use of this project is to act as a menu-driven progam that acts a
# simple library system that can be used to return, add, and view all books
# inside the library system.

# Creating start function.
def start():
    # Initializing a list, to hold bookname, ISBN, Author, Edition, and Borrowers.
    allBooks = [
        ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
        ['9780134494166', "The Human Body", "Dave R", 1, []],
        ['9780321125217', "Human on Earth",
            "Jordan P", 1, ['David', 'b1', 'user123']]
    ]
    # Initializing list to hold rented ISBNS.
    borrowedISBNS = []
    user_selection = ""  # Initializing variable to hold user selection.

    # Start of while loop to continute to ask user for input until they exit.
    while user_selection != 'x' and user_selection != '5':

        printMenu()  # Calls printMenu function to give user options.
        # takes user selection input from menu.
        user_selection = str(input("Your selection> ")).lower()

        # Calls validSelection to make sure it is a correct input option.
        user_selection = validSelection(user_selection)

        # If statment checks what selection is given and provides the right response.
        if user_selection == 'a' or user_selection == '1':
            check = True  # Initalizes check
            one_new_book = addNewBook()  # Calls addbook function.
            # Checks if they provided a real ISBN.
            if one_new_book[0] == 'False':
                print("Invalid ISBN")
                continue
            else:
                for i in range(0, len(allBooks)):
                    # Checks if the ISBN is already with a book.
                    if str(allBooks[i][0]) == str(one_new_book[0]):
                        print("Duplicate ISBN is found! Cannot add the book.")
                        check = False
                if check == True:
                    # Adds new book to all books.
                    allBooks.append(one_new_book)
                    print("\nA new book is added successfully.")

        elif user_selection == 'r' or user_selection == '2':
            # Calls borrowBooks function to let the user borrow books.
            borrowed_books = borrowBooks(allBooks, borrowedISBNS)
            # If no books were found to borrow it gives the user an error message.
            if not bool(borrowed_books):
                print("No books found!")
                continue
            else:  # It tells the user the books was successfully borrowed.
                for x in range(0, len(borrowed_books)):
                    print("-\"" + str(borrowed_books[x]) + "\" is borrowed!")

        elif user_selection == 't' or user_selection == '3':
            # Calls returnbook function to let users return owned books.
            returned_book = returnBook(borrowedISBNS, allBooks)
            # If a invalid books was found it gives the user and error.
            if not bool(returned_book):
                print("No book is found!")
                continue
            else:  # Provides feedback letting the user know the book was successfully returned.
                for x in range(0, len(returned_book)):
                    print("\"" + returned_book[0] + "\" is returned.")

        elif user_selection == 'l' or user_selection == '4':
            # Calls function to print a list of all avaliable books.
            listOfBooks(allBooks, borrowedISBNS)
    # Print a final list of all books to the user once they exit the program.
    print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
    listOfBooks(allBooks, borrowedISBNS)

# Defines printMenu fuction, Prints the menu layout to the usre


def printMenu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')

# Defines validSelection function, make sure user inputs a correct selection response


def validSelection(user_selection):
    check = True  # Initalizes check function

    # Checks to see if the user selection is a correct response
    if user_selection != 'a' and user_selection != 'r' and user_selection != 't' and user_selection != 'l' and user_selection != 'x' and user_selection != '1' and user_selection != '2' and user_selection != '3' and user_selection != '4' and user_selection != '5':
        check = False

    # If they don't input a correct response it will continue to ask the user to input a correct response
    while check == False:
        print("\nWrong Selection! Please select a valid option.")
        printMenu()
        user_selection = str(input("Your selection> ")).lower()
        if user_selection == 'a' or user_selection == 'r' or user_selection == 't' or user_selection == 'l' or user_selection == 'x' or user_selection == '1' or user_selection == '2' or user_selection == '3' or user_selection == '4' or user_selection == '5':
            check = True

    # Returns the users correct response
    return user_selection

# Defines addNewBook function, it allows the user to put more books into the library


def addNewBook():
    # Initializes book_name and asks user to input the name of the book
    book_name = str(input("Book name> "))

    # Makes sure the book name does not contain a * or % and will keep asking the user to input a correct input
    while '*' in book_name or '%' in book_name:
        print("Invalid book name!")
        book_name = str(input("Book name> "))

    # Asks user for author name
    author = str(input("Author name> "))

    # Asks user for edition of the book
    edition = input("Edition> ")

    # Makes sure the edition is a integer value
    while not edition.replace('.', '', 1).isdigit():
        print("Invalid Edition!")
        edition = input("Edition> ")

    # Converts edition with decimals to intgers
    edition = int(float(edition))

    # Asks user for ISBN
    ISBN_number = input("ISBN> ")
    # Calls isbnCheck to make sure it is a valid ISBN
    ISBN_number = ISBNCheck(ISBN_number)

    # Collects all book data and contains it in a string
    one_new_Book = [str(ISBN_number), book_name, author, edition, []]

    # Returns book values
    return one_new_Book

#  Defines ISBN check function, makes sure ISBN is valid


def ISBNCheck(ISBN_num):
    # Checks to ssee if ISBN is 13 digits, it will contiue to ask if not
    while not ISBN_num.isdigit() or len(ISBN_num) != 13:
        print("INVALID ISBN")
        ISBN_num = input("ISBN> ")

    ISBN_num = str(ISBN_num)  # Converts ISBN to a string

    if validISBN(ISBN_num) == False:  # calls validIsbn to see the weight factor for validity
        return False

    return int(ISBN_num)

# Checks valdity of ISBN


def validISBN(x):
    total = 0

    # Checks validity by multiplying it by a weight factor
    for i in range(0, len(x)):
        if i % 2 == 0:
            total = total + (int(x[i])*1)
        elif i % 2 == 1:
            total = total + (int(x[i])*3)

    # Checks if toal is a mutliple of 10
    if total % 10 == 0:
        return True

    # Returns either true or false if it is a valid ISBN
    return False

# Defines borrowBooks function to allow user to borrow books


def borrowBooks(x, y):
    # Asks user for borrower name and the serch term
    borrower_name = str(input("Enter the borrower name> "))
    search_term = str(input("Search term> ")).lower()
    # Initalizes borrowed_books to nothing
    borrowed_books = ""

    # Checks what type of search type the want and returns the according books
    if "*" in search_term:
        borrowed_books = contains(x, search_term, y, borrower_name)
        return borrowed_books
    elif "%" in search_term:
        borrowed_books = startsWith(x, search_term, y, borrower_name)
        return borrowed_books
    else:
        borrowed_books = exact(x, search_term, y, borrower_name)
        return borrowed_books

# Defines contains, the function borrows books with the term being in any word of the book


def contains(books, term, rented, name):
    check = True  # Intializes check
    temp = []  # Initalizes temp list to store books

    # Replaces the * with nothing to use to compare
    term = term.replace("*", "")
    for i in range(0, len(books)):
        # Looks through each word to check if its in the book name
        if term in (str(books[i][1]).lower()):
            for j in range(0, len(rented)):
                # Checks if book is not already rented
                if str(books[i][0]) == str(rented[j]):
                    check = False
            if check == True:  # If book is not rented it adds ISBN to rented books, and adds borrower to borrower history
                temp.append(books[i][1])
                books[i][4].append(name)
                rented.append(books[i][0])
        check = True
    return temp

# Defines startWith, the function borrows books with the term being the first in the book


def startsWith(books, term, rented, name):
    check = True  # Intializes check
    temp = []  # Initalizes temp list to store books
    check_word = ""  # Initlizes check word, to compare with term

    # Replaces the % with nothing to use to compare
    term = term.replace("%", "")

    # Program to find books that match serch term with the first word of the book
    for i in range(0, len(books)):
        if term in (str(books[i][1]).lower()):
            temp2 = str(books[i][1]).lower()
            check_word = temp2.split()  # Splits name of book into list
            if (term == check_word[0]):  # Sees if first word in book is the term
                for j in range(0, len(rented)):
                    # Checks if book is not already rented
                    if str(books[i][0]) == str(rented[j]):
                        check = False
                if check == True:  # If book is not rented it adds ISBN to rented books, and adds borrower to borrower history
                    temp.append(books[i][1])
                    books[i][4].append(name)
                    rented.append(books[i][0])
        check = True
    return temp

# Defines exact function, lets user borrow books with their exact input


def exact(books, term, rented, name):
    check = True  # Initalizes check, to see if books is alreay rented
    temp = []  # Intializes temp list to store the books to borrow
    check_book = ""  # Initalizes check_ book to compare it existing books

    # Program to find books that match serch term to the exact text
    for i in range(0, len(books)):
        if term in (str(books[i][1]).lower()):
            check_book = str(books[i][1]).lower()
            if (term == check_book):  # Makes sure books exists
                for j in range(0, len(rented)):
                    # Checks if book is not already rented
                    if str(books[i][0]) == str(rented[j]):
                        check = False
                if check == True:  # If book is not rented it adds ISBN to rented books, and adds borrower to borrower history
                    temp.append(books[i][1])
                    books[i][4].append(name)
                    rented.append(books[i][0])
        check = True
    return temp  # Returns

# Defines returnBook function, that allows user to return books


def returnBook(rented, books):
    # Initalizes matched_isbns (One that is already stored), and returend_book (the book they are returning)
    matched_ISBN = []
    returned_book = []

    # Asks user for the ISBN they want to return
    returned_ISBN = str(input("ISBN> "))

    # Finds the ISBN and book that they want to return
    for i in range(len(rented)):
        if returned_ISBN == rented[i]:
            matched_ISBN.append(i)
            for x in range(len(books)):
                if returned_ISBN == books[x][0]:
                    returned_book.append(books[x][1])
    # Removes ISBN from borrowedISBNS
    for j in range(len(matched_ISBN)):
        rented.pop(matched_ISBN[j])

    return returned_book

# Defines listOfBooks, and prints out all the books and if they are avaliable or not


def listOfBooks(books, rented):
    # Initalizes avaliablity
    availablity = "Available"

    # Checks if book is avaliable or not
    for i in range(len(books)):
        for x in range(len(rented)):
            if rented[x] == books[i][0]:
                availablity = "Unavailable"
        # Prints out the book with all the information and if it is avaliable (Formatted)
        print("---------------")
        print("[" + availablity + "]")
        print(books[i][1] + " - " + books[i][2])
        print("E: " + str(books[i][3]) + " ISBN: " + str(books[i][0]))
        print("Borrowed by: ", end="")
        print(books[i][4])
        availablity = "Available"


# Calls start function
start()
