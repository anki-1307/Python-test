

class BookCollectionManager:
    def __init__(self):
        self.books = {}

    def add_book(self, title, quantity):
        if not title or quantity <= 0:
            print("Invalid title or quantity. Please try again.")
            return
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        print(f"Added '{title}' with quantity {quantity}.")

    def remove_book(self, title, quantity):
        if title not in self.books:
            print(f"'{title}' not found in the collection.")
            return
        if quantity <= 0:
            print("Invalid quantity. Please enter a positive number.")
            return
        if self.books[title] <= quantity:
            del self.books[title]
            print(f"'{title}' has been removed from the collection.")
        else:
            self.books[title] -= quantity
            print(f"Decreased quantity of '{title}' by {quantity}. Remaining: {self.books[title]}.")

    def view_collection(self):
        if not self.books:
            print("The book collection is empty.")
            return
        print("Book Collection:")
        for title, quantity in self.books.items():
            print(f"Title: {title}, Quantity: {quantity}")

    def total_books(self):
        total = sum(self.books.values())
        print(f"Total number of books in the collection: {total}")

def main():
    manager = BookCollectionManager()

    while True:
        print("\nOptions:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View Book Collection")
        print("4. Total Books Available")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter book title: ")
            try:
                quantity = int(input("Enter quantity: "))
                manager.add_book(title, quantity)
            except ValueError:
                print("Invalid input. Quantity should be a number.")
        elif choice == '2':
            title = input("Enter book title: ")
            try:
                quantity = int(input("Enter quantity to remove: "))
                manager.remove_book(title, quantity)
            except ValueError:
                print("Invalid input. Quantity should be a number.")
        elif choice == '3':
            manager.view_collection()
        elif choice == '4':
            manager.total_books()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()




















