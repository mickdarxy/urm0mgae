#indicate a variable that shows whether program runs or not
running = True

#define a function that searches a book within the data given
def search_book(books, term):
    for book in books:
        if term.lower() in book['title'].lower() or term.lower() in book['author'].lower() or term.lower() in book['publisher'].lower():
           return True

#create a function that adds a book given the string
def add_book(books):
    # book title, book author, publisher, publication date
    books_input = input("Enter book details: (title, author, publisher, pub_date): ")
    title, author, publisher, pub_date = map(str.strip, books_input.split(','))
    entering_new_book = {'title': title, 'author': author, 'publisher': publisher, 'pub_date': pub_date}
    if not search_book(books, title):
        books.append(entering_new_book)
        print("book has been added")
    else:
        print("book already exists in this list")

#main function to display for user
def main():
    books = []
    while True:
        print("[A] Add Book")
        print("[S] Search book")
        print("[E] Exit (and print")
        choice = input("what would you like to do?: ")
        if choice == "A":
            entering_new_book = input("Enter Book Details: ")
        elif choice == "S":
            entering_new_book = input("Search Book: ")
        elif choice == "E":
            running = False
        else:
            print("Invalid Input")

