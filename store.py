from catalog import catalog 

cart = []

def print_header(text):
    print("\n\n\n")
    print("-------------------------")
    print(text)
    print("-------------------------")


def print_menu():
    print("Menu")
    print(" 1.- View Catalog")
    print(" 2.- Search Products")
    print(" 3.- View Cart")
    print(" 4.- Checkout")
    print(" 5.- Clear Cart")
    print(" 6.- Add Item")
    print("")
    print(" Q.- Quit")


def print_catalog():
    print_header("- Our Catalog -")
    for prod in catalog:
        #print(str(prod["id"]) + " " + prod["title"] + " $" + str(prod["price"]))
        print(f"| {prod["id"]} | {prod["title"].ljust(12)} | ${prod["price"]} |")
    answer=input("Type ID to add (N to close): ")
    if answer == "n" or answer == "N":
        return # finish the fn
    else:
        add_product_to_cart(answer)
    

def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == prod_id:
            found = True
            cart.append(prod)
            print(f'{prod["title"]} added to cart!')

    if not found:
        print("** Error: Invalid ID")    


def search_product():
    text = input("Search text: ")
    found = False
    for prod in catalog: # checking every product in the catalog
        if text in prod["title"]:
            found = True
            print(f'Found: ID {prod["id"]} | {prod["title"]} | ${prod["price"]}')
            choice = input("Do you want to add item to cart? (y/n): ")
            if choice == "y":
                add_product_to_cart(str(prod["id"]))
        
    if not found:
        print("Sorry, this item doesn't exist")


def view_cart():
    print_header("Your Cart")
    if not cart:
        print("Your cart is empty.")
    else:
        for prod in cart:
            print(f"| {prod["id"]} | {prod["title"].ljust(12)} | ${prod["price"]} |")


def cart_total():
    total = 0
    for prod in cart:
        total += prod["price"]
    print(f"Total: ${total}")    


def checkout():
    if not cart:
        print("Your cart is empty")
        return
    
    print_header("Checkout")
    name = input("Enter your Full Name: ")
    email = input("Enter your Email: ")
    phoneNum = input("Enter your Phone Number: ")
    
    cart_total()
    print("Thank you for your purchace!")
    clear_cart()


def clear_cart():
    if not cart:
        print("Your cart is already empty")
        return
    else:
        cart.clear()
    print("Your cart has been cleared.")


def add_item_to_catalog():
    try:
        prod_id = int(input("Enter product ID: "))
        title = input("Enter product Title: ")
        price = float(input("Enter product Price: "))
        new_prod = {"id": prod_id, "title": title, "price": price}
        catalog.append(new_prod)
        print(f'product "{title}" Product has been added."')
    except ValueError:
        print("**Error")
    



#### initialize
option = ""
while option != "q" and option != "Q":
    print_header("Welcome to Store xy")
    print_menu()

    option=input("Choose an option: ")
    #print("User selected: " + option)

    if option == "1":
        print_catalog()
    elif option == "2":
        search_product()
    elif option == "3":
        view_cart() 
        cart_total()
    elif option == "4":
        checkout()
    elif option == "5":
        clear_cart()
    elif option == "6":
        add_item_to_catalog()
    elif option == "q" or option == "Q":
        print("Good Bye")
    else:
        print("** Error: Invalid Option")
