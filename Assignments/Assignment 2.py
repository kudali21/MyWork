#!/usr/bin/env python
# coding: utf-8

# In[ ]:


users_db = {}

clothing_items = {
    1: {"item": "T-Shirt", "category": "shirt", "gender": "male", "style": "casual", "price": 499},
    2: {"item": "Formal Shirt", "category": "shirt", "gender": "male", "style": "formal", "price": 899},
    3: {"item": "Denim Jeans", "category": "pants", "gender": "male", "style": "casual", "price": 1199},
    5: {"item": "Scarf", "category": "accessory", "gender": "female", "style": "trendy", "price": 299},
    6: {"item": "Crop Top", "category": "shirt", "gender": "female", "style": "casual", "price": 599},
    7: {"item": "Formal Trousers", "category": "pants", "gender": "female", "style": "formal", "price": 999},
    8: {"item": "Oversized Hoodie", "category": "shirt", "gender": "unisex", "style": "casual", "price": 1299}
}

print("=== Welcome to H&M Fashion Portal ===")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter username: ")
        if username in users_db:
            print("Username already exists!")
            continue
        password = input("Enter password: ")
        users_db[username] = {"password": password}
        print("Registration successful!")

    elif choice == "2":
        username = input("Enter username: ")
        if username not in users_db:
            print("User not found. Please register.")
            continue
        password = input("Enter password: ")
        if users_db[username]["password"] != password:
            print("Incorrect password!")
            continue

        print(f"\nWelcome, {username}!")

        # Asking preferences only after login
        gender = input("Enter your gender (male/female/unisex, 0 to go back): ").lower()
        if gender == "0":
            continue
        style = input("Preferred style (casual/formal/trendy, 0 to go back): ").lower()
        if style == "0":
            continue
        budget_input = input("Enter your average clothing budget (₹, 0 to go back): ")
        if budget_input == "0":
            continue
        budget = int(budget_input)

        while True:
            print("\n1. View Recommended Clothing")
            print("2. Shop Now")
            print("3. Logout")
            print("0. Go Back")
            option = input("Choose an option: ")

            if option == "0":
                break

            elif option == "1":
                print("\nRecommended Clothing Based on Your Preferences:")
                recommended = {}
                for id, item in clothing_items.items():
                    match_gender = item["gender"] == gender or item["gender"] == "unisex"
                    match_style = item["style"] == style
                    within_budget = item["price"] <= budget
                    if match_gender and match_style and within_budget:
                        print(f"{id}. {item['item']} - ₹{item['price']} ({item['style'].capitalize()} / {item['category']})")
                        recommended[id] = item

                if not recommended:
                    print("No items match your preferences.")
                    continue

                add_choice = input("Do you want to add any of these to your cart? (yes/no): ").lower()
                if add_choice == "yes":
                    selection_input = input("Enter item numbers to add to cart (space separated, 0 to cancel): ")
                    if selection_input == "0":
                        continue
                    selection = list(map(int, selection_input.split()))
                    cart = {}
                    for i in selection:
                        if i in recommended:
                            if i in cart:
                                cart[i] += 1
                            else:
                                cart[i] = 1
                        else:
                            print(f"Item ID {i} not in recommendations. Skipping.")

                    if cart:
                        print("\n--- Cart Summary ---")
                        total = 0
                        for id, qty in cart.items():
                            item_name = clothing_items[id]["item"]
                            price = clothing_items[id]["price"]
                            print(f"{item_name} x {qty} = ₹{price * qty}")
                            total += price * qty

                        print(f"\nTotal Items: {sum(cart.values())}")
                        print(f"Total Amount: ₹{total}")
                        confirm = input("Do you want to place the order? (yes/no): ").lower()
                        if confirm == "yes":
                            print("Booking Successful! Your stylish items are on the way 💃🛍️")
                            cont = input("Do you want to continue shopping? (yes/no): ").lower()
                            if cont == "no":
                                print("Thank you for shopping with H&M!")
                                exit()
                        else:
                            print("Booking Cancelled.")
                    else:
                        print("No valid items selected.")

            elif option == "2":
                print("\nAvailable Clothing Items:")
                for id, item in clothing_items.items():
                    print(f"{id}. {item['item']} - ₹{item['price']} ({item['style']} / {item['gender']})")

                selection_input = input("Enter item numbers to add to cart (space separated, 0 to go back): ")
                if selection_input == "0":
                    continue
                selection = list(map(int, selection_input.split()))
                cart = {}
                for i in selection:
                    if i in cart:
                        cart[i] += 1
                    else:
                        cart[i] = 1

                if cart:
                    print("\n--- Cart Summary ---")
                    total = 0
                    for id, qty in cart.items():
                        item_name = clothing_items[id]["item"]
                        price = clothing_items[id]["price"]
                        print(f"{item_name} x {qty} = ₹{price * qty}")
                        total += price * qty

                    print(f"\nTotal Items: {sum(cart.values())}")
                    print(f"Total Amount: ₹{total}")
                    confirm = input("Do you want to place the order? (yes/no): ").lower()
                    if confirm == "yes":
                        print("Booking Successful! Your stylish items are on the way 💃🛍️")
                        cont = input("Do you want to continue shopping? (yes/no): ").lower()
                        if cont == "no":
                            print("Thank you for shopping with H&M!")
                            exit()
                    else:
                        print("Booking Cancelled.")
                else:
                    print("No valid items selected.")

            elif option == "3":
                print("Logged out successfully.")
                break

    elif choice == "3":
        print("Thank you for visiting H&M Fashion! ")
        break

    else:
        print("Invalid option. Please try again.")


# In[ ]:





# In[ ]:




