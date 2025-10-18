from catalog import catalog
menu_header = """
===============================
===========Main Menu===========
==============================="""

menu = [menu_header, "1. - View Catalog", "2. - Search Products", "3. - View Cart", "4. - CLear Cart", "Q. - Quit"]
cart = []

def print_header(text):
    print(text)

def print_menu():
    for item in menu:
        print(item)

def print_catalog():
    print("""
===========================
========OUR CATALOG========
===========================""")
    print(f"#     Item             Price")
    for item in catalog:
        print(f"| {item["id"]} | {item["title"].ljust(15)}  |${item["price"]/100}|")
    selected_prod = input("Choose a product to add (N to close): ")
    if selected_prod.lower == "n":
        return
    else: 
        add_product_to_cart(selected_prod)

def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod_id) == str(prod["id"]):
            found = True
            cart.append(prod)
            break
    print("Item added to cart")
    print(f"| {prod["id"]} | {prod["title"].ljust(15)}  |${prod["price"]/100}|")
    if not found:
        print("Error - invalid option")

def view_cart():
    print("""
===============================
===========Your Cart===========
===============================""")
    if not cart:
        print("Cart is empty")
    else:
        for item in cart:
            print(f"| {item["id"]} | {item["title"].ljust(15)}  |${item["price"]/100}|")
        total = get_cart_total(cart)
        print(f"Total cart price = ${total/100}")
    
def search_products():
    text = input("Search text: ")
    found = False
    for prod in catalog:
        if text.lower() in prod["title"].lower():
            found = True
            print("Product Found: ")
            print(f"| {prod["id"]} | {prod["title"].ljust(15)}  |${prod["price"]/100}|")
            add_prod = input("Do you want to add this to your cart (y/n)")
            if add_prod.lower() == "y":
                add_product_to_cart(prod["id"])
    if not found:
        print("Product not found")

def get_cart_total(cart):
    total = 0
    for prod in cart:
        item_cost = int(prod["price"])
        total = total + item_cost
    return total

def clear_cart():
    cart.clear()
    view_cart()
   
# MAIN LOOP
print_header("Welcome to the Store")
options = ""
while options.lower() != "q":
    print_menu()
    
    options = input("Choose an option: ")

    if options == "1":
        print_catalog()
    elif options == "2":
        search_products()
    elif options == "3":
        view_cart()
    elif options == "4":
        clear_cart()
    elif options.lower() == "q":
        print(menu[3])
    else:
        print("try again")