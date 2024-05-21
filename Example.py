import os

class Supermarket:
    def __init__(self):
        self.food_products = [
            {"name": "apples", "price": 2.5},
            {"name": "bananas", "price": 1.8},
            {"name": "grapes", "price": 3.0},
            {"name": "carrots", "price": 1.0},
            {"name": "lettuce", "price": 1.5},
            {"name": "tomatoes", "price": 2.0},
            {"name": "chicken", "price": 5.0},
            {"name": "beef", "price": 7.0},
            {"name": "pork", "price": 6.0}
        ]

        self.toiletry_products = [
            {"name": "soap", "price": 2.0},
            {"name": "shampoo", "price": 3.5},
            {"name": "toothpaste", "price": 2.0}
        ]

        self.current_purchase = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_main_menu(self):
        self.clear_screen()
        print("Welcome to the supermarket!")
        print("Select an option:")
        print("1. Food")
        print("2. Toiletries")
        print("3. View Receipt")
        print("4. Exit")

    def show_available_products(self, products):
        self.clear_screen()
        print("Available Products:")
        for idx, product in enumerate(products):
            print(f"{idx + 1}. {product['name'].capitalize()} - ${product['price']}")
        print("0. Back to main menu")

        while True:
            choice = input("Select a product or press Enter to go back: ")
            if choice.isdigit():
                choice = int(choice)
                if choice >= 1 and choice <= len(products):
                    quantity = input("How many do you want to buy? (Enter a number): ")
                    try:
                        quantity = int(quantity)
                        total_price = products[choice - 1]["price"] * quantity
                        self.add_product(products[choice - 1]["name"], products[choice - 1]["price"], quantity)
                        print(f"\nYou have added {quantity} {products[choice - 1]['name']} to your cart.")
                        input("\nPress Enter to continue...")
                        break
                    except ValueError:
                        input("Invalid quantity. Press Enter to go back...")
            elif choice == "":
                break
            else:
                input("Invalid product. Press Enter to go back...")

    def add_product(self, name, price, quantity):
        self.current_purchase.append({"name": name, "price": price, "quantity": quantity})

    def view_receipt(self):
        self.clear_screen()
        print("Receipt:")
        total_amount = 0
        for item in self.current_purchase:
            item_total = item["price"] * item["quantity"]
            total_amount += item_total
            print(f"{item['quantity']} {item['name']} - ${item_total}")
        print("\nTotal Amount:", total_amount)
        input("\nPress Enter to continue...")

    def main(self):
        while True:
            self.show_main_menu()
            option = input("Enter your choice: ")

            if option == "1":
                self.show_available_products(self.food_products)
            elif option == "2":
                self.show_available_products(self.toiletry_products)
            elif option == "3":
                self.view_receipt()
            elif option == "4":
                self.clear_screen()
                print("Thank you for visiting the supermarket. Goodbye!")
                break
            else:
                input("Invalid option. Press Enter to return to the main menu...")

if __name__ == "__main__":
    supermarket = Supermarket()
    supermarket.main()
