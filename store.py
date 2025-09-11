from catalog import catalog 


def print_header(text):
    print("-------------------------")
    print(text)
    print("-------------------------")


def print_menu():
    print("Menu")
    print(" 1.- View Catalog")
    print(" 2.- Search Products")
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
            print("Found")

    if not found:
        print("** Error: Invalid ID")    


def search_product():
    text = input("Search text: ")
    print(text)


#### initialize
print_header("Welcome to Store xy")
print_menu()

option=input("Choose an option: ")
#print("User selected: " + option)

if option == "1":
    print_catalog()
elif option == "2":
    search_product()
elif option == "q" or option == "Q":
    print("Good Bye")
else:
    print("** Error: Invalid Option")
