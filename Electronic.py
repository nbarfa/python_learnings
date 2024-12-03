class ElectronicItem:
    def __init__(self, name, brand, model, price, year, specifications):
        self.name = name
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.specifications = specifications

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")
        print(f"Year: {self.year}")
        print(f"Specifications: {self.specifications}")


def input_details():
    name = input("Enter the name of the electronic item: ")
    brand = input("Enter the brand: ")
    model = input("Enter the model: ")
    price = input("Enter the price: ")
    year = input("Enter the year of manufacture: ")
    specifications = input("Enter the specifications: ")
    return ElectronicItem(name, brand, model, price, year, specifications)


def display_all_items(items):
    if not items:
        print("No electronic items available.")
    else:
        for index, item in enumerate(items):
            print(f"\nItem {index + 1}:")
            item.display_details()


def main():
    items = []
    while True:
        print("\nWhat do you want to do?")
        print("1. Fill in the details of a new electronic item.")
        print("2. See the devices available in the program.")
        print("3. Exit.")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            item = input_details()
            items.append(item)
        elif choice == '2':
            display_all_items(items)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
