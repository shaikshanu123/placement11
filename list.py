# Initialize empty cart list
cart = []

while True:
    # Single print for menu
    print("""
--- Cart Menu ---
1. Add Item
2. View All Items
3. Search Item
4. Remove Item
5. Exit
""")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter item to add: ")
        cart.append(item)
        print(f"'{item}' added to cart.")

    elif choice == "2":
        if cart:
            print("Items in your cart:")
            for i, item in enumerate(cart, start=1):
                print(f"{i}. {item}")
        else:
            print("Your cart is empty.")

    elif choice == "3":
        search_item = input("Enter item to search: ")
        if search_item in cart:
            print(f"'{search_item}' is in your cart.")
        else:
            print(f"'{search_item}' not found in your cart.")

    elif choice == "4":
        remove_item = input("Enter item to remove: ")
        if remove_item in cart:
            cart.remove(remove_item)
            print(f"'{remove_item}' removed from cart.")
        else:
            print(f"'{remove_item}' not found in your cart.")

    elif choice == "5":
        print("Exiting cart. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-5.")
