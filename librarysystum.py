import datetime

class LMS:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({
                str(Id): {
                    "books_title": line.strip(),
                    "lender_name": "",
                    "Issue_date": "",
                    "Status": "Available"
                }
            })
            Id += 1

    def display_books(self):
        print("\n------------------ List of Books ----------------")
        print("Books_Id\tTitle")
        print("-------------------------------------------------")
        for key, value in self.books_dict.items():
            print(f"{key}\t\t{value['books_title']} - [{value['Status']}]")

    def Issue_books(self):
        books_id = input("Enter book ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict:
            if self.books_dict[books_id]['Status'] != "Available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['Issue_date']}")
            else:
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Already issued"
                print("Book issued successfully!\n")
        else:
            print("Book ID not found!")

    def add_books(self):
        new_book = input("Enter book title: ")
        if new_book == "":
            return self.add_books()
        elif len(new_book) > 25:
            print("Book title is too long! Limit is 25 characters.")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as bk:
                bk.write(f"{new_book}\n")
            new_id = str(int(max(self.books_dict)) + 1)
            self.books_dict[new_id] = {
                "books_title": new_book,
                "lender_name": "",
                "Issue_date": "",
                "Status": "Available"
            }
            print(f"The book '{new_book}' has been added successfully.")

    def Return_books(self):
        books_id = input("Enter book ID: ")
        if books_id in self.books_dict:
            if self.books_dict[books_id]['Status'] == "Available":
                print("This book is already in the library.")
            else:
                self.books_dict[books_id]['lender_name'] = ""
                self.books_dict[books_id]['Issue_date'] = ""
                self.books_dict[books_id]['Status'] = "Available"
                print("Book returned successfully!\n")
        else:
            print("Book ID not found!")

    def search_books(self):
        search_term = input("Enter book title to search: ").lower()
        found = False
        print("\n------------------ Search Results ----------------")
        print("Books_Id\tTitle\t\t\tStatus")
        print("--------------------------------------------------")
        for book_id, details in self.books_dict.items():
            if search_term in details['books_title'].lower():
                print(f"{book_id}\t\t{details['books_title'][:25]:<25} - [{details['Status']}]")
                found = True
        if not found:
            print("No matching books found.")

# Run the LMS system
try:
    myLMS = LMS("List_of_books.txt", "Python's")
    press_key_list = {
        "D": "Display Books",
        "I": "Issue Books",
        "S": "Search Book",
        "A": "Add Books",
        "R": "Return Books",
        "Q": "Quit"
    }

    key_press = ""
    while key_press.lower() != "q":
        print(f"\n-------- Welcome to {myLMS.library_name} Library Management System --------\n")
        for key, action in press_key_list.items():
            print(f"Press {key} to {action}")
        key_press = input("Press key: ").lower()

        if key_press == "d":
            myLMS.display_books()
        elif key_press == "i":
            myLMS.Issue_books()
        elif key_press == "s":
            myLMS.search_books()
        elif key_press == "a":
            myLMS.add_books()
        elif key_press == "r":
            myLMS.Return_books()
        elif key_press == "q":
            print("Exiting system. Goodbye!")
        else:
            print("Invalid option. Try again.")

except Exception as e:
    print("Something went wrong! Please check your input.")
    print("Error:", e)
