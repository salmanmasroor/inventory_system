from product import Product
from inventory import Inventory

inv = Inventory()

while True:
    price = None
    quantity = None
    print("\n=== INVENTORY SYSTEM ===")
    print("1. Add Product")
    print("2. View Product")
    print("3. Delete Product")
    print("4. Update Product")
    print("5. Exit")

    option = input("Enter Choice: ")

    if option == "1":
        product_name  = input("Enter the Product Name: ")
        while price is None:
            try:
                price = float(input("Enter the Price: "))
            except ValueError:
                print("Invalid price. Please enter a numeric/decimal value.")

        while quantity is None:
            try:
                quantity = int(input("Enter the Qty: "))
            except ValueError:
                print("Invalid quantity. Please enter an integer value.")
        
        product = Product(product_name,price,quantity)

        print(product)
        inv.add_product(product)
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
        try:
            product_id = int(input("Enter the Product ID to delete:"))
            inv.delete_product(product_id)
            print("Product deleted!")
        except ValueError:
            print("Invalid ID. Please enter an integer value.")
    elif option == "4":
        try:
            product_id = int(input("Enter the Product ID to Update:"))
            print("What you want to Update")
            print("1. Name")
            print("2. Price")
            print("3. Quantity")
            choice = int(input("Enter to Choose:"))
            data = inv.select_option(choice)
            value = input("Enter the value: ")
            inv.update_product(product_id,data,value)
            print("updated !")
        except ValueError:
            print("Error")
    elif option == "5":
        print("Closed!")
        break

    else:
        print("Invalid Choice")