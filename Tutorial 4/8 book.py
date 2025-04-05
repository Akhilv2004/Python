class Book:
    def get_details(self):
        self.title = input("Enter book title: ")
        self.author = input("Enter author: ")
        self.cost = float(input("Enter cost: "))

    def print_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Cost: ${self.cost}")

book = Book()
book.get_details()
book.print_details()
