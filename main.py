from product import Product
from inventory import Inventory

inv = Inventory()

while True:
    print("\n=== INVENTORY SYSTEM ===")
    print("1. Add Product")
    print("2. View Product")
    print("3. Exit")

    option = input("Enter Choice: ")

    if option == "1":
        product_name  = input("Enter the Product Name: ")
        price = float(input("Enter the Price: "))
        quantity = int(input("Enter the Qty: "))
        p = Product(product_name,price,quantity)
        inv.add_product(p)
        print("Product added!")
    
    elif option == "2":
        data = inv.view_products()
        print("ID  | Product Name | Quanity  | Price")
        print("--------------------------------------")

        for row in data:
            print(
                str(row[0]).ljust(3),
                "|",
                str(row[1]).ljust(12),
                "|",
                str(row[3]).ljust(8),
                "|",
                str(row[2])
            )
    elif option == "3":
        print("Closed!")
        break
    
    else:
        print("Invalid Choice")