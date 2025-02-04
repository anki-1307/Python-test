# Book Management System

class BookCollection:
    def __init__(self):
        self.books = {}

    def add_book(self,title,quantity):
        if title in self.books:
            self.books[title] += quantity

        else:
            self.books[title] = quantity

        print(f"Books added {quantity} available of name {title} ")


    def remove_book(self,title):
        if title in self.books:
            del self.books[title]
            print(f"Removed books {title} from collection")
        else:
            print(f"{title} book not available in collection")

    def decrease_quantity(self,title,quantity):
        if title in self.books:
            if self.books[title] > quantity :
                self.books[title] -=quantity
                print(f"Decreased no of {quantity} of book {title}.")

            elif self.books [title] == quantity:
                del self.books[title]
                print(f"Book {title} removed from collection")

            else:
                print(f"{title} is not available in bookcollection")

    def view_books(self):
            if not self.books:
                print("Thre are no books available in collection")
            else:
                print("Books present in collection")

                for title,quantity in self.books.items():
                    print(f" books available {title} : {quantity} present")

    def total_books(self):
            total = sum(self.books.values())
            print("Books in the collection : {total}")
            for title,quantity in self.books.items():
                print(f" {title}: {quantity} present in collection")
            print(f"Total books available in collection: {total}")

    def main ():
        collection = BookCollection()

        while True:
            print("Book Collection")
            print("\n 1. Add Book")
            print("\n 2. Remove Book")
            print("\n 3.No of decreased books")
            print("\n 4.View Book Collection")
            print("\n 5. Total Books")
            print("\n 6. Exit ")

            choice = input("Enter your choice : ")
            if choice == "1":
                title=input("Enter Book title: ")
                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity <= 0:
                        print("Quantity must be positive")
                    else:
                        collection.add_book(title,quantity)
                except ValueError:
                    print("Please enter a valid number for quantity")

            elif choice == "2":
                title =input("Enter Book title to remove: ")

                collection.remove_book(title)
            elif choice == "3":
                title=input("Enter book title: ")
                try:
                    quantity = int(input("Enter quantity to decrease: "))

                if quantity <=0 :
                    print("Quantity must be a positive number")
                else:
                    collection.decrease_quantity(title,quantity)

                except ValueError:
                    print("Please enter no of quantity")

            elif choice == "4":
                collection.view_books()
            elif choice == "5":
                collection.total_books()
            elif choice == "6":
                print("Exit")


if __name__ == "__main__":
    main()



















