# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15),
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450),
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8),
    ],
}

# products_list = list(products.items())


def display_sorted_products(products_list, sort_order):
    # Sort products based on the given order
    if sort_order == "asc":
        sorted_products = sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        sorted_products = sorted(products_list, key=lambda x: x[1], reverse=True)

    # Display sorted products
    for i, product in enumerate(sorted_products, 1):
        print(f"{i}. {product[0]} - ${product[1]}")

    return sorted_products


def display_products(products_list):
    print("Products available:")
    for i, product in enumerate(products_list, 1):
        print(f"{i}. {product[0]} - ${product[1]}")


def display_categories():
    categories = list(products.keys())
    print("Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    category = input(f"Please enter a category: ")
    if category.isdigit():
        result = int(category) - 1
    else:
        result = None
    return result


def add_to_cart(cart, product, quantity):
    cart.append(tuple(list(product) + [quantity]))


def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return

    total_cost = 0
    print("--- Cart Contents ---")
    for item in cart:
        total_cost += item[1] * item[2]
        print(f"{item[0]} - ${item[1]} x {item[2]} = ${item[1] * item[2]}")

    print(f"Total cost: ${total_cost}")


def generate_receipt(name, email, cart, total_cost, address):
    print("--- Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Products:")
    for item in cart:
        print(f"{item[0]} (x{item[1]}) - ${item[2]}")
    print(f"Total cost: ${total_cost}")
    print(f"Delivery address: {address}")
    print(
        "Your items will be delivered in 3 days. Payment will be accepted after successful delivery."
    )


def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)


def validate_email(email):
    result = "@" in email
    return result


def main():
    name = input("Enter your full name (first and last name): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid first and last name containing only letters.")
        name = input("Enter your full name (first and last name): ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address containing '@'.")
        email = input("Enter your email address: ")

    cart = []
    total_cost = 0

    while True:
        category_choice = display_categories()

        selected_category = list(products.keys())[category_choice - 1]
        products_list = products[selected_category]

        while True:
            display_products(products_list)

            print("Options:")
            print("1. Select a product to buy")
            print("2. Sort products by price")
            print("3. Go back to category selection")
            print("4. Finish shopping")

            option = int(input("Choose an option (1-4): "))
            if option == 1:
                product_choice = int(input("Select a product by number: "))

                product = products_list[product_choice - 1]
                quantity = int(input(f"Enter quantity for {product[0]}: "))
                add_to_cart(cart, product, quantity)
                total_cost += product[1] * quantity
                print(f"Added {quantity} of {product[0]} to your cart.")

            elif option == 2:
                sort_order = int(
                    input("Sort by price: 1 for ascending, 2 for descending: ")
                )

                display_sorted_products(products_list, sort_order)

            elif option == 3:
                break

            elif option == 4:
                if cart:
                    display_cart(cart)
                    print(f"Total cost: ${total_cost}")
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day")
                return


""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
