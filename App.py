# Continuation from W4
# Will persist Data into a MYSQL database and refactor code

# Importing string for capwords() operation, used to capitalize words
import string

# Importing only the 'system' function from the 'os' module to use system-specific commands
from os import system, name

# Importing 'sleep' to pause or delay the program execution for a specified time period
from time import sleep

# Importing 're' module for regular expression operations, useful for string pattern matching
import re

# Importing functions from other local modules:
# 'create_tables' from 'db_setup' - used to create necessary database tables
from db_setup import create_tables

# 'connect_db' from 'db_connection' - used to establish a connection to the database
from db_connection import connect_db


#=================================================== SETTING UP CONNECTION ========================================================================

def main():
    print("Setting up the database...")
    create_tables()
    # You can add more functionality here, like interacting with products or orders

if __name__ == "__main__":
    main()


#===================================================== MAIN DEFINITIONS =============================================================================
line = "==================================================================================="

def bye():
    sleep(2)
    clear_screen()
        
def clear_screen():  #clear the terminal in between 
    system("cls" if name == "nt" else "clear")


def call_products_list():  # Get product list from the database
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")  # Adjust the table name accordingly
    products = cursor.fetchall()
    cursor.close()
    db.close()
    return products
    

def append_product(name, price):  # Append a product to the database
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO products (Name, Price) VALUES (%s, %s)", (name, price))
    db.commit()
    cursor.close()
    db.close()

from db_connection import connect_db

def show_prod_list():
    connection = connect_db()
    if connection:
        cursor = connection.cursor(dictionary=True)  # Fetch results as dictionaries for better readability
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        print(line)
        print("                                     PRODUCTS LIST")
        print(line)

        for product in products:
            print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}")
        print(line)

        cursor.close()
        connection.close()
        return products  # Return the list of products for further use

                    

def update_product(name, price):  # Update a product in the database
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("UPDATE products SET Price = %s WHERE Name = %s", (price, name))
    db.commit()
    cursor.close()
    db.close()

def call_couriers_list():  # Get couriers list from the database
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM couriers")  # Adjust the table name accordingly
    couriers = cursor.fetchall()
    cursor.close()
    db.close()
    return couriers

def update_couriers(courier_list):
    db = connect_db()
    cursor = db.cursor()
    try:
        for courier in courier_list:
            # Use the correct column names
            sql = "UPDATE couriers SET phone_number = %s WHERE name = %s"
            params = (courier["phone_number"], courier["name"])
            cursor.execute(sql, params)
        db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        db.close()



def append_courier(name, phone_number):  # Append a courier to the database
    db = connect_db()
    cursor = db.cursor()

    # Get the next available id
    cursor.execute("SELECT MAX(id) FROM couriers")
    max_id = cursor.fetchone()[0] or 0  # If no records exist, start from 0
    new_id = max_id + 1

    # Insert new courier with explicit id
    cursor.execute("INSERT INTO couriers (id, Name, Phone_Number) VALUES (%s, %s, %s)", (new_id, name, phone_number))
    db.commit()
    cursor.close()
    db.close()


def couriers():
    print(line)
    print("                                     COURIERS LIST")
    print(line)
    couriers_list = call_couriers_list()

    for courier in couriers_list:
        print(f'Courier Id: {courier["id"]}')  # Display the courier ID
        print(f'Courier Name: {courier["name"]}')  # Display the name with a user-friendly label
        print(f'Courier Phone Number: {courier["phone_number"]}')  # Display the phone number with a user-friendly label
        print(line)


    

def call_orders_list():  # Get orders list from the database
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders")  # Adjust the table name accordingly
    orders = cursor.fetchall()
    cursor.close()
    db.close()
    return orders
 

def update_order(order_id, customer_name, customer_address, customer_phone, order_status, courier, items):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE orders SET Customer_Name = %s, Customer_Address = %s, Customer_Phone_Number = %s, Order_Status = %s, Courier = %s, Items = %s WHERE id = %s",
        (customer_name, customer_address, customer_phone, order_status, courier, items, order_id)
    )
    db.commit()
    cursor.close()
    db.close()

    

def append_order(customer_name, customer_address, customer_phone, order_status, courier, items):
    db = connect_db()
    cursor = db.cursor()

    # Get the maximum existing id
    cursor.execute("SELECT MAX(id) FROM orders")
    max_id = cursor.fetchone()[0] or 0  # If no orders exist, start from 0
    new_id = max_id + 1  # Increment to get the new id

    # Insert the new order with the explicit id
    cursor.execute(
        "INSERT INTO orders (id, Customer_Name, Customer_Address, Customer_Phone_Number, Order_Status, Courier, Items) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (new_id, customer_name, customer_address, customer_phone, order_status, courier, items)
    )

    db.commit()
    cursor.close()
    db.close()


def print_order_list():
    print(line)
    print("                                     ORDERS LIST")
    print(line)
    
    # Friendly display names for the fields
    display_names = {
        'id': 'Order Id',
        'customer_name': 'Customer Name',
        'customer_address': 'Customer Address',
        'customer_phone_number': 'Customer Phone Number',
        'order_status': 'Order Status',
        'courier': 'Courier Id',
        'items': 'Items'
    }
    
    orders_list = call_orders_list()
    for order in orders_list:
        # No need to print Order Index, assuming `id` field is already present
        for key, value in order.items():
            # Use the display name if it exists, otherwise default to the key
            print(f'{display_names.get(key, key)}: {value}')
        print(line)


def another_service():
    while True:
        user_fouth_inp = (input("Would you like another service? Y/N: ").upper())
        if user_fouth_inp == "Y":
            sleep(2)
            clear_screen()
            show_full_menu()  # You may need to define this function
        elif user_fouth_inp == "N":
            print(line)
            print("Thank you for visiting Dunkin Donuts")
            exit()
        else:
            print(line)
            print("That was not a valid selection, please try again.")



#======================================================= MENUS ==============================================================================================

main_menu = ['0: Main Menu', '1: Save Product, Courier and Order lists then Exit App']
def show_main_menu():
    print(f'{line} \n\nPlease select the corresponding value between 0-1 from one of the following options:') 
    
    for i in main_menu:
         print()
         print(i)
    print()
    print(line) 
  
    user_selection = input("What will be your selection?: ")

    if user_selection == "1":
        print("Thank you for visiting our store")
        sleep(2)
        system('cls')
        exit()  

    elif user_selection == "0":
        sleep(2)
        clear_screen()
        show_full_menu()
        
    else:
        sleep(1)
        print(line)
        print("That was not a valid selection, please try again")
        show_main_menu()


full_menu = ['0: Orders Menu', '1: Products Menu', '2: Couriers Menu', '3: Back']
def show_full_menu():
   
    print(line)
    print("                                     MAIN MENU")
    print(line) 
    for i in full_menu:
        print()
        print(i)
    print()
    print(line)
    user_full_inp = input ("What selection would you like to make from the above?: ")
    if user_full_inp == "0":
        sleep(2) 
        clear_screen()
        show_orders_menu()
    elif user_full_inp == "1":
        sleep(2)
        clear_screen()
        show_second_menu()
    elif user_full_inp == "3":
        sleep(2)
        clear_screen()
        show_main_menu()
    elif user_full_inp == "2":
        sleep(2)
        clear_screen()
        show_courier_menu()
    else:
        print(line)
        print()
        print("That was not a valid selection, please try again.")
        print()
        sleep(2)
        clear_screen()
        show_full_menu()



second_menu = ['0: Product List', '1: Create New Product', '2: Update Existing Product', '3: Delete Product', '4: Back' ]
def show_second_menu():
        print(line)
        print("                                     PRODUCTS MENU")
        print(line)

        for i in second_menu: 
            print()
            print(i)
        print()
        print(line)
        user_second_inp = input("What selection would you like to make from the above?: ")
        if user_second_inp== "4":
            bye()
            show_full_menu()
        elif user_second_inp == "0":
            bye()
            run_products_menu()
        elif user_second_inp == "1":
            bye()
            create_new_product()
            another_service()
        elif user_second_inp == "2":
            bye()
            update_existing_product()
            another_service()
        elif user_second_inp == "3":
            bye()
            delete_product()
            another_service()
        else:
            print(line)
            print("\nThat was not a valid selection, please try again.\n")
            show_second_menu()



#======================================================= PRODUCTS ===================================================================================================================
# product_list = ['0: Strawberry', '1: Chocolate', '2: Raspberry', '3: Vanilla', '4: Glazed']

def run_products_menu():
    print(line)
    products = show_prod_list()  # Get the products list from the database

    while True:
        try:
            print()
            # Prompt the user to select a product by its ID
            user_input = int(input("Which product would you prefer? \n\nPlease enter the corresponding Product ID: "))
            
            # Check if the entered Product ID exists in the database
            selected_product = next((p for p in products if p['id'] == user_input), None)

            if selected_product:
                sleep(2)
                clear_screen()
                print(f"Your order for '{selected_product['name']}' has been placed! It will be with you shortly!")
                print()
                another_service()  # Call another service or function as needed
                break
            else:
                print(line)
                print("\nInvalid Product ID! Please select a valid ID from the list: \n")

        except ValueError:
            print(line)
            print("\nNot a valid number! Please enter a valid Product ID: \n")



def create_new_product():
    while True:
        connection = connect_db()  # Establish connection to the database
        if connection:
            cursor = connection.cursor()
            try:
                # Get user input for the product name
                user_input_name = string.capwords(str(input('What will this product be called?: ')))

                # Check if the name contains only alphabetic characters and spaces
                if not all(x.isalpha() or x.isspace() for x in user_input_name):
                    print("\nError: Invalid name. Please ensure the name contains only alphabetic characters or spaces.")
                    continue  # Re-run the loop if the name is invalid

                # Get user input for the product price
                user_input_price = input('How much will this product cost?: ')

                # Ensure price is a valid float with up to 2 decimal places
                try:
                    user_input_price = float(user_input_price)
                    user_input_price_str = str(user_input_price)
                    integral, fractional = user_input_price_str.split('.')

                    if len(fractional) > 2:
                        print("\nError: Invalid price format. Please use up to 2 decimal places.")
                        continue  # Re-run the loop if the price format is invalid
                except ValueError:
                    print("\nError: Invalid input. Please enter a valid number for the price.")
                    continue  # Re-run the loop if the price is not a number

                # Get the next available id
                cursor.execute("SELECT MAX(id) FROM products")
                max_id = cursor.fetchone()[0] or 0  # If no records exist, start from 0
                new_id = max_id + 1

                # Insert new product with explicit id
                query = "INSERT INTO products (id, name, price) VALUES (%s, %s, %s)"
                cursor.execute(query, (new_id, user_input_name, user_input_price))
                connection.commit()
                print(f"Product {user_input_name} has been added.")
                break  # Exit the loop after successful insertion

            except Exception as e:
                print(f"\nError: {e}")

            finally:
                # Ensure cursor and connection are always closed
                cursor.close()
                connection.close()



   

def update_existing_product():
    connection = connect_db()  # Connect to the database
    if connection:
        cursor = connection.cursor(dictionary=True)
        
        # Fetch product list from the database
        cursor.execute("SELECT * FROM products")
        products_list = cursor.fetchall()
        
        while True:
            # Display all products
            print(line)
            show_prod_list()
            
            # Ask user to select a product by ID
            try:
                product_id = int(input("Enter the ID of the product you would like to update: "))
                selected_product = next((p for p in products_list if p["id"] == product_id), None)

                if selected_product:
                    print(f"You have selected: {selected_product['name']} (Price: ${selected_product['price']})")
                    print(line)
                    
                    # Get updated information
                    new_name = input(f"Enter the updated Product name (leave blank to keep '{selected_product['name']}'): ") or selected_product['name']
                    new_price = input(f"Enter the updated Product price (leave blank to keep '{selected_product['price']}'): ") or selected_product['price']

                    # Validate the updated price
                    try:
                        new_price = float(new_price)
                        new_price_str = str(new_price)
                        integral, fractional = new_price_str.split('.')

                        if len(fractional) <= 2:
                            # Update product in the database
                            query = "UPDATE products SET name=%s, price=%s WHERE id=%s"
                            cursor.execute(query, (new_name, new_price, product_id))
                            connection.commit()

                            print(f"\nProduct {product_id} has been updated to: Name: {new_name}, Price: {new_price}")
                            print(line)
                            print("This is the updated Product list:")
                            show_prod_list()
                            break  # Exit loop after successful update
                        else:
                            print("\nError: Price should have up to two decimal places.")
                    except ValueError:
                        print("\nError: Invalid price format.")
                else:
                    print(f"\nError: No product found with ID {product_id}. Please try again.")

            except ValueError:
                print("\nError: Invalid product ID. Please enter a valid number.")

        # Close the connection
        cursor.close()
        connection.close()


def delete_product():
    while True:  # Start an infinite loop
        print(line)
        products = show_prod_list()  # Fetch and display the product list from the database
        
        user_select = input('Enter the ID of the product you would like to delete (or type "exit" to cancel): ')  # Ask for the product ID
        
        if user_select.lower() == "exit":  # Allow user to exit
            print("Operation cancelled.")
            break
        
        # Validate user input
        if user_select.isdigit():
            product_id = int(user_select)
            # Check if the product exists in the fetched list
            if any(product['id'] == product_id for product in products):
                connection = connect_db()  # Connect to the database
                if connection:
                    cursor = connection.cursor()
                    try:
                        # Delete the product from the database
                        query = "DELETE FROM products WHERE id = %s"
                        cursor.execute(query, (product_id,))
                        connection.commit()
                        
                        print(f'{line}\nProduct ID {product_id} has been deleted successfully!\n{line}')
                        show_prod_list()
                        break  # Exit the loop after successful deletion
                    except Exception as e:
                        print(f"\nError: {e}")
                    finally:
                        cursor.close()
                        connection.close()  # Ensure cursor and connection are closed
            else:
                print(f'{line}\nInvalid product ID. Please try again!')
        else:
            print(f'{line}\nInvalid input. Please enter a numeric ID.')




#================================================ ORDERS ==========================================================================================================
orders_options = [
    '0: Orders list', 
    '1: Create new Order', 
    '2: Update existing Order Status', 
    '3: Update existing Order', 
    '4: Delete Order', 
    '5: Filter Orders',  # New option for filtering orders
    '6: Back'  
]

def show_orders_menu():
    print(line)
    print("                                     ORDERS MENU")
    print(line)
    for i in orders_options: 
        print()
        print(i)
    print()
    print(line)
    
    user_order_inp = input("What selection would you like to make from the above?: ")
    
    if user_order_inp == "6":  # To go back to last menu
        sleep(2)
        system('cls')
        show_full_menu()      
    elif user_order_inp == "0":  # Print orders
        bye()
        print_order_list()
        another_service()
    elif user_order_inp == "1":  # ADD new order
        bye()
        create_new_order()
    elif user_order_inp == "2":  # Update existing order status
        bye()
        update_existing_order_status()
        print_order_list()
        another_service()
    elif user_order_inp == "3":  # Update existing order
        bye()
        update_existing_order()
        print_order_list()
        another_service()
    elif user_order_inp == "4":  # Delete order
        bye()
        delete_existing_order()
        print_order_list()
        another_service()
    elif user_order_inp == "5":  # Filter orders
        bye()
        filter_orders()  # Call filter orders function
        another_service()
    else:
        print(line)
        print("That was not a valid selection, please try again.")
        bye()
        show_orders_menu()


def filter_orders():
    while True:  # Start an infinite loop
        print("Filter orders by:")
        print("1. Order Status")
        print("2. Courier")
        print("3. Back")  # Add an option to go back to the previous menu
        choice = input("Please select an option (1, 2, or 3): ")
        
        if choice == '1':
            # List possible order statuses
            print(line)
            print("\nPossible Order Statuses:")
            print("1. Preparing")
            print("2. Ready")
            print("3. Shipped")
            print("4. Delivered")
            
            status_choice = input("Select the order status by number (1-4): ")
            status_map = {
                '1': 'Preparing',
                '2': 'Ready',
                '3': 'Shipped',
                '4': 'Delivered'
            }
            
            status = status_map.get(status_choice)
            if status:
                display_orders_by_status(status)
                
            else:
                print("Invalid status selected. Please try again.")

        elif choice == '2':
            couriers()  # Display the list of couriers
            
            # Select courier by ID
            try:
                courier_id = int(input("Enter the courier ID to filter by: "))  # Convert input to integer
                display_orders_by_courier(courier_id)
                print(line)
            except ValueError:
                print("Invalid input. Please enter a valid integer for courier ID.")

        elif choice == '3':
            print("Returning to the previous menu...")
            break  # Exit the loop if the user chooses to go back

        else:
            print(line)
            print()
            print("Invalid option selected. Please try again.")
            print()

def display_orders_by_courier(courier_id):
    orders = call_orders_list()  # Fetch the list of orders
    filtered_orders = [order for order in orders if order.get("courier") == courier_id]  # Compare as integers
    
    if not filtered_orders:
        print(f"No orders found for courier ID '{courier_id}'.")
    else:
        print(f"Orders assigned to courier ID '{courier_id}':")
        for order in filtered_orders:
            print_order_details(order)  # Use a helper function
            print('-' * 40)  # Separator line



def display_orders_by_status(status):
    orders = call_orders_list()  # Fetch the list of orders
    filtered_orders = [order for order in orders if order.get("order_status") == status]
    
    if not filtered_orders:
        print(f"No orders found with status '{status}'.")
    else:
        print(line)
        print(f"Orders with status '{status}':")
        for order in filtered_orders:
            print_order_details(order)  # Use a helper function for formatted output
            print(line)


def print_order_details(order):
    """Helper function to print order details in a user-friendly format."""
    print("Order Details:")
    print(f"  Order Id: {order.get('id', 'N/A')}")  # Default to 'N/A' if key doesn't exist
    print(f"  Customer Name: {order.get('customer_name', 'N/A')}")
    print(f"  Order Status: {order.get('order_status', 'N/A')}")
    print(f"  Courier ID: {order.get('courier', 'N/A')}")
    print(f"  Delivery Address: {order.get('customer_address', 'N/A')}")
    print(f"  Item Id: {order.get('items', 'N/A')}")
    

def create_new_order():
    customer_name = input("What is the Full Name?: ")
    customer_address = input("What is the Address: ")
    customer_phone = input("What is the Telephone No.?: ")

    if isinstance(customer_name, str) and len(customer_name) > 0:
        if not customer_phone.isdigit() or len(customer_phone) != 11: 
            print("Please insert a valid telephone number consisting of 11 digits")
            create_new_order()
        else:
            print(line)
            print()
            print("These are the products currently available:")
            print()
            print(line)
            show_prod_list()

            # Get the list of products once for validation
            products_list = call_products_list()  
            max_product_id = len(products_list)  # Assume product IDs start at 1 and are sequential.

            while True:
                product_select = input("What are the IDs of the products you would like to purchase?\n(Please list each product ID separated by a comma): ")
                
                # Removing spaces and using regex to extract numbers from input
                nums = [int(n.replace(',', '').strip()) for n in re.findall(r'[\d,]+', product_select)]

                # Validate the input: check that each product ID is within range (1 to max_product_id)
                if all(c.isdigit() or c == "," for c in product_select.replace(' ', '')) and all(1 <= int(d) <= max_product_id for d in nums):

                    couriers()
                    while True:
                        courier_select = input("What is the index of the courier you would like to use?: ")
                        if courier_select.isdigit() and 1 <= int(courier_select) <= len(call_couriers_list()):  # Adjusted for 1-based index
                            order = {
                                "Customer Name": customer_name,
                                "Customer Address": customer_address,
                                "Phone Number": customer_phone,
                                "Order Status": "Preparing",
                                "Courier": courier_select,
                                "Items": product_select  # Keeping original input as selected IDs
                            }

                            # Define the fields and append the order
                            fields = ['Customer Name', 'Customer Address', 'Phone Number', 'Order Status', 'Courier', 'Items']
                            append_order(customer_name, customer_address, customer_phone, order['Order Status'], courier_select, product_select)

                            print(line)
                            print()
                            print("\nOrder created successfully!\n")
                            print()
                            print(line)
                            print()
                            print("This is the updated Orders list:")
                            print_order_list()
                            another_service()
                            break
                        else:
                            print("\nThat is an invalid courier index. Please try again.")
                else:
                    print("\nThat is an invalid product ID. Please try again.")
    else:
        print("Please insert a valid name.")
        create_new_order()



def update_existing_order_status():
    while True:  # Start an infinite loop to allow retries
        print_order_list()
        user_select = input('What is the index of the order you would like to change the status of? (1 to {}): '.format(len(call_orders_list())))

        # Ensure user_select is a valid index (1-based index)
        orders = call_orders_list()  # Get the list of orders once
        if user_select.isdigit() and 1 <= int(user_select) <= len(orders):
            bye()
            print(line)
            print("                                     ORDERS STATUSES")
            print(line)
            statuses = ["Preparing", "Ready", "Shipped", "Delivered"]
            
            order_index = int(user_select) - 1  # Convert user input to 0-based index
            order = orders[order_index]  # Get the order details

            # Display the current status
            current_status = order.get('order_status', 'Unknown')  # Use .get() to avoid KeyError
            print(f'\nCurrent Order Status: {current_status}')
            print("\nAvailable statuses:")
            for count, status in enumerate(statuses):
                print(f'{count}: {status}')

            new_status = input('Enter the new status (0-3) or leave blank to keep the current status: ')
            if new_status.isdigit() and 0 <= int(new_status) <= 3:
                order['order_status'] = statuses[int(new_status)]  # Update status
            elif new_status == "":
                print("Keeping current order status.")
            else:   
                print("\nThat is an invalid status index. Please try again.")
                continue  # Restart the loop to try again
            
            # Proceed with the update
            if 'id' in order and 'customer_name' in order and 'customer_address' in order and 'customer_phone_number' in order:
                order_id = order['id']  # Assuming there is an 'id' field
                update_order(
                    order_id, 
                    order['customer_name'], 
                    order['customer_address'], 
                    order['customer_phone_number'], 
                    order['order_status'],  # Use updated status here
                    order['courier'], 
                    order['items']
                )
                
                print()
                print(line)
                print()
                print("\nOrder Status updated successfully!\n")
                bye()
                return  # Exit the function after successful update
            else:
                print("\nOrder does not contain required fields. Please check the data structure.")
                break  # Exit the inner loop
        else:
            print("\nThat is an invalid order index. Please try again.")
            # The outer loop will cause it to run again if the order index is invalid

        

def update_existing_order(): 
    print_order_list()
    user_select = input('What is the Id of the order you would like to change? (1 to {}): '.format(len(call_orders_list())))
    var = call_orders_list()
    
    # Change the condition to allow only IDs starting from 1
    if user_select.isdigit() and 1 <= int(user_select) <= len(var):
        print()
        print(line)
        print("Please provide updated information for the following")
        bye()
        
        order_index = int(user_select) - 1  # Convert to zero-based index
        order = var[order_index]  # Get the current order
        
        while True:
            new_name = input(f'Current Name: {order.get("customer_name", "N/A")}\nPlease enter the updated name (leave blank to keep the same): ')
            new_address = input(f'Current Address: {order.get("customer_address", "N/A")}\nPlease enter the updated address (leave blank to keep the same): ')
            new_phone = input(f'Current Phone Number: {order.get("customer_phone_number", "N/A")}\nPlease enter the updated phone number (leave blank to keep the same): ') 
            
            # Update fields only if new values are provided
            if new_name:
                if new_name.isalpha() and len(new_name) > 0:  # Check if the name is valid
                    order["customer_name"] = new_name
                else:
                    print(f'{line}\nPlease insert a valid name')
                    continue  # Skip the rest of the loop and ask again
            
            if new_address:  # Keep the current address if input is blank
                order["customer_address"] = new_address
            
            if new_phone:
                if new_phone.isdigit() and len(new_phone) == 11:  # Check if phone number is valid
                    order["customer_phone_number"] = new_phone
                else:
                    print(f'{line}\nPlease insert a valid telephone number consisting of 11 digits')
                    continue  # Skip the rest of the loop and ask again
            
            # Update the order in the database
            order_id = order['id']  # Assuming there is an 'id' field
            update_order(
                order_id, 
                order["customer_name"], 
                order["customer_address"], 
                order["customer_phone_number"], 
                order["order_status"],  # Assuming the order status is unchanged
                order["courier"], 
                order["items"]
            )
            
            bye()
            print(f'{line} \nCustomer information updated successfully as follows!\n')          
            for key, value in order.items():
                print(f'{key}: {value}')
            print()
            print(line)

            print("This is the updated Orders List")
            print_order_list()
            break
    else:
        print(f"\nInvalid order index. Please select a value between 1 and {len(var)}")
        update_existing_order()  # Allow the user to try again




def delete_existing_order():
    print_order_list()
    user_select = input('What is the index of the order would you like to Delete?: ')
    var = call_orders_list()

    # Ensure that user can only select an index starting from 1 (matching the order IDs)
    if user_select.isdigit() and 1 <= int(user_select) <= len(var):
        # Convert user input (which starts from 1) to zero-based index for list lookup
        order_id = var[int(user_select) - 1]['id']  # Adjust for zero-based indexing
        confirm_delete = input(f'Are you sure you want to delete order ID {order_id}? (y/n): ')
        if confirm_delete.lower() == 'y':
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
            db.commit()
            cursor.close()
            db.close()
            print(f"\nOrder ID {order_id} deleted successfully!")
        else:
            print("\nDeletion canceled.")
    else:
        print("\nThat is an invalid index. Please try again.")
        delete_existing_order()


#=========================================== COURIERS ==========================================================================
courier_options = ['0: Courier list', '1: Create new Courier', '2: Update existing Courier',  
                  '3: Delete Courier', '4: Back' ]

def show_courier_menu():
    print(line)
    print("                                   COURIERS MENU")
    print(line)
    for i in courier_options: 
        print()
        print(i)
    print()
    print(line)
    print()
    user_courier_inp = input("What selection would you like to make from the above?: ")
    print()
    if user_courier_inp == "0":  # Print Courier list
        bye()
        couriers()
        another_service()
    elif user_courier_inp == "1":  # Create new courier
        bye()
        create_new_courier()
    elif user_courier_inp == "2":  # Update existing Courier
        bye()
        update_existing_courier()
        another_service()
    elif user_courier_inp == "3":  # Delete Courier
        bye()
        delete_couriers()
        another_service()
    elif user_courier_inp == "4":  # Back
         sleep(2)
         system('cls')
         show_full_menu()
    else:
        bye()
        print(line)
        print()
        print("That was not a valid selection, please try again.")
        print()
        show_courier_menu()

def create_new_courier():
    while True:
        try:
            print(line)
            user_input_name = string.capwords(str(input('What is the name of the Courier?: ')), sep=None)
            user_input_number = input('What is the Telephone No.? ')
            print()
            if user_input_name.isalpha() and len(user_input_number) == 11 and user_input_number.isdigit():
                append_courier(user_input_name, user_input_number)
                print(line)
                print("\nNew Courier Added to list successfully!\n")
                print(line)
                print("This is the updated Couriers List")
                couriers()
                another_service()
                break  # Exit loop after successful addition
            else:
                print("Please insert a valid name and telephone number consisting of 11 digits")
                
        except ValueError:
            print("Please Try Again!")

def update_existing_courier():
    couriers()  # Display the current list of couriers
    
    user_select = input('What is the index of the Courier you would like to change? (1 to {}) : '.format(len(call_couriers_list())))
    couriers_list = call_couriers_list()
    
    # Change this line to check for the range based on 1 indexing
    if user_select.isdigit() and 1 <= int(user_select) <= len(couriers_list):
        print(line)
        print()
        print("Please provide updated information for the below")
        print()
        
        # Get the current courier information
        current_courier = couriers_list[int(user_select) - 1]
        
        while True:
            new_name = input(f'Current Name: {current_courier["name"]}\nPlease enter the updated name (leave blank to keep the same): ')
            new_phone = input(f'Current Phone Number: {current_courier["phone_number"]}\nPlease enter the updated phone number (leave blank to keep the same): ')
            
            # Update the courier information if provided, else keep the current value
            if new_name:
                if new_name.isalpha():  # Checks if Name entered contains no integers.
                    current_courier["name"] = new_name
                else:
                    print(line)
                    print()
                    print(f'{line}\nPlease insert a valid name')
                    continue  # Skip the rest of the loop and ask again
            
            if new_phone:
                if new_phone.isdigit() and len(new_phone) == 11:  # Checks if number entered is 11 digits
                    current_courier["phone_number"] = new_phone
                else:
                    print(line)
                    print()
                    print(f'{line}\nPlease insert a valid telephone number consisting of 11 digits')
                    continue  # Skip the rest of the loop and ask again
            
            # Successfully updated or kept the same values
            print(f'{line} \n\nCourier information updated successfully as follows:\n')
            print(line)
            print()
            print(f'Courier Name: {current_courier["name"]}')
            print(f'Phone Number: {current_courier["phone_number"]}')
            update_couriers(couriers_list)  # Call function to update the database
            print()
            print(line)
            print()
            print("The updated List is as follows:")
            print()
            couriers()
            break
    else:
        print(line)
        print()
        print(f"\nInvalid courier index. Please select a value between 1 and {len(couriers_list)}")
        update_existing_courier()  # Allow the user to try again


def delete_couriers():
    couriers()  # Display the current list of couriers
    user_select = input('What is the index of the Courier you would like to delete? (1 to {}): '.format(len(call_couriers_list())))
    couriers_list = call_couriers_list()
    
    # Check if the input is a digit and falls within the valid range (1 to length of couriers_list)
    if user_select.isdigit() and 1 <= int(user_select) <= len(couriers_list):
        # Identify the courier to delete
        courier_to_delete = couriers_list[int(user_select) - 1]
        print(f'Preparing to delete: {courier_to_delete}')  # Debugging line

        # Call the delete function
        delete_courier_from_db(courier_to_delete)

        # Now update the couriers list in memory after deletion
        del couriers_list[int(user_select) - 1]
        
        print()
        print(f'{line}\nCourier list updated successfully!\nThis is the updated list:\n')
        couriers()  # Display the updated list of couriers
    else:   
        print(f'{line}\nInvalid index. Please try again.')
        delete_couriers()  # Allow the user to try again

def delete_courier_from_db(courier):
    db = connect_db()
    cursor = db.cursor()
    try:
        # Assuming there is a unique identifier for each courier, e.g., "id"
        sql = "DELETE FROM couriers WHERE name = %s AND phone_number = %s"
        params = (courier["name"], courier["phone_number"])
        cursor.execute(sql, params)
        db.commit()
        print(f'Courier {courier["name"]} deleted from the database.')
    except Exception as e:
        print(f"An error occurred while deleting: {e}")
    finally:
        cursor.close()
        db.close()


# ==================================================================================================================================================================================


#                           oi YOU! Yes, YOU!
# THE FUN STARTS HERE!!! (only 3 lines.. I know, but don't be deceived. It's smoll but mighty!)
print(line)
print()
print('                        Welcome to Dunkin Donuts! ^_^')
print()
show_main_menu()

