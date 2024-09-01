#Continuation from W3

# importing string for capswords() operation to capitalise words
import string

# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# csv functions to write to csv files
import csv
from csv import DictWriter

import re

#===================================================== MAIN DEFINITIONS ===========================================================================================
line = "==================================================================================="

def bye():
    sleep(2)
    clear_screen()
        
def clear_screen():  #clear the terminal in between 
    system("cls" if name == "nt" else "clear")


def call_products_list(a): #This function runs the above but with an argument i give it
    #creates list
    return Test1(a)
     
class Test1:
     def __init__(self , a ):
        with open("products.csv", a, newline ='' )  as products_list_file: #opens the products list txt fil
            self.first = products_list_file #select this if i want to do operations on the file
            if a != "w":
                self.second = csv.DictReader(products_list_file) #reads the products list file - select this if i want this
                self.third = list(self.second)
           

      
def append_courier_list(a, z): #This function runs the above but with an argument i give it
    with open("couriers.csv", a) as file:
        file.write(z)
        file.close()


def append_prod_list(a, z, l): #This function runs the above but with an argument i give it
    with open("products.csv", a) as file:
        dictwriter_object = DictWriter(file, fieldnames=l)
        dictwriter_object.writerow(z)
        file.close()


def prods():
    print(line)
    print("                                     PRODUCTS LIST")
    print(line)
    for x, v in enumerate(call_products_list("r").third):
        print (f'Product Index: {x}')
        for key,value in v.items():
            print (f'{key}: {value}')
        print (line)

                    
def update_products_csv(x): 
    myFile = open('products.csv', 'w') #call_products_list("w").first
    writer = csv.writer(myFile)
    writer.writerow(['Name', 'Price($)'])
    for dictionary in x:
        writer.writerow(dictionary.values())
    myFile.close()


def call_couriers_list(a): #This function runs the above but with an argument i give it
    #creates list
    return Test2(a)

class Test2:
     def __init__(self , a ):
        with open("couriers.csv", a, newline ='' )  as couriers_list_file: #opens the products list txt fil
            self.first = couriers_list_file #select this if i want to do operations on the file
            if a != "w":
                self.second = csv.DictReader(couriers_list_file) #reads the products list file - select this if i want this
                self.third = list(self.second)


def append_couriers_list(a, z, l): #This function runs the above but with an argument i give it
    with open("couriers.csv", a) as file:
        dictwriter_object = DictWriter(file, fieldnames=l)
        dictwriter_object.writerow(z)
        file.close()

def couriers():
    print(line)
    print("                                     COURIERS LIST")
    print(line)
    for x, v in enumerate(call_couriers_list("r").third):
        print (f'Courier Index: {x}')
        for key,value in v.items():
            print (f'{key}: {value}')
        print (line)

    

def save_csv_filese(): #TO save files?? -CHECK WORKS
    couriers_list_file = open("couriers.csv", "a") #opens the products list txt file
    couriers_list_file.close()

    products_list_file = open("products.csv", "a") 
    products_list_file.close()

    orders_list_file= open("orders.csv", "a") 
    orders_list_file.close()

 

def another_service():
    while True:
                user_fouth_inp= (input("Would you like another service? Y/N: ").upper())
                if user_fouth_inp == "Y":
                    sleep(2)
                    clear_screen()
                    show_full_menu() 
                elif user_fouth_inp == "N":
                    print(line)
                    print("Thank you for visiting Dunkin Donuts")
                    exit()
                else:
                    print(line)
                    print("That was not a valid selection, please try again. ")

def call_orders_list(a): #This function runs the above but with an argument i give it
    #creates list
    return Test3(a)

class Test3:
     def __init__(self , a ):
        with open("orders.csv", a, newline ='' )  as orders_list_file: #opens the products list txt fil
            self.first = orders_list_file #select this if i want to do operations on the file
            if a != "w":
                self.second = csv.DictReader(orders_list_file) #reads the products list file - select this if i want this
                self.third = list(self.second)

def print_order_list():
    print(line)
    print("                                     ORDERS LIST")
    print(line)
    for x, v in enumerate(call_orders_list("r").third):
        print (f'Customer Index: {x}')
        for key,value in v.items():
            print (f'{key}: {value}')
        print (line)
        
def update_couriers_csv(x): 
    myFile = open('couriers.csv', 'w')
    writer = csv.writer(myFile)
    writer.writerow(['Name', 'Phone Number'])
    for dictionary in x:
        writer.writerow(dictionary.values())
    myFile.close()

            
                    
def update_orders_csv(x): 
    myFile = open('orders.csv', 'w') #call_products_list("w").first
    writer = csv.writer(myFile)
  
    writer.writerow(['Customer Name', 'Customer Address', 'Customer Phone Number', 'Order Status',  'Courier', 'Items'])
    
    for dictionary in x:
        writer.writerow(dictionary.values())
    myFile.close()
    
def append_orders_list(a, z, l): #This function runs the above but with an argument i give it
    with open("orders.csv", a) as file:
        dictwriter_object = DictWriter(file, fieldnames=l)
        dictwriter_object.writerow(z)
        file.close()



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
        save_csv_filese()
        print("Thank you for visiting our store")
        sleep(2)
        system('cls')
        exit()  

    elif user_selection == "0":
        sleep(2)
        clear_screen()
        show_full_menu()
        
    else:
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
            show_prod_list()
        elif user_second_inp == "1":
            bye()
            create_new_product()
        elif user_second_inp == "2":
            bye()
            update_existing_product()
        elif user_second_inp == "3":
            bye()
            delete_product()
        else:
            print(line)
            print("\nThat was not a valid selection, please try again.\n")
            show_second_menu()



#======================================================= PRODUCTS ===================================================================================================================
# product_list = ['0: Strawberry', '1: Chocolate', '2: Raspberry', '3: Vanilla', '4: Glazed']

def show_prod_list():
    print(line)
    prods()
    while True:
        try: 
            print()
            user_third_inp = int(input("Which Donut would you prefer amongst the above? \n\nPlease select the corresponding Index value for your order: "))
            oki = user_third_inp
            var = call_products_list("r")
            assert  oki in ((range(len((var.third)))))
            sleep(2)
            clear_screen()
            print ("Your order will be with you shortly!")
            print()
            another_service ()
        except ValueError:
            print(line)
            print("\nNot a Value! Please select the corresponding Index value for your order: \n")
            show_prod_list()
        except AssertionError:
            print(line)
            print("\nNot a Value within range! Please select the corresponding value for your order: \n")
            show_prod_list()
        else:
            break


def create_new_product():
    while True:
        try:
            user_input_name = string.capwords(str(input('What will this product be called?: ')), sep = None)
            user_input_price = float(input('How much will this product cost?: '))
            user_input_price = str(user_input_price)
            integral, fractional = (user_input_price).split('.')
            if user_input_name.isalpha():
                if not 0<= len(fractional) <=2 :
                    print(line)
                    print("\nError: Invalid price\nPlease Try Again!")
                    sleep(2)
                    clear_screen()
                else:
                    product = {
                            "Name": user_input_name,
                            "Price($)": user_input_price
                        }
                    fields = ['Name', 'Price($)']
                    append_prod_list("a", product, fields)
                    print("\nOrder created successfully!\n")
                    prods()
                    another_service()
            else:
                print("\nError: Invalid Name\nPlease Try Again!")
                sleep(2)
                clear_screen()
        except ValueError: 
            print("\nPlease Try Again\n")
   
    

def update_existing_product():
    print(line)
    prods()
    print()
    ask_customer = input("What is the index of the product you would you like to update?: ")
    var1 = call_products_list("r")
    products_list_file = var1.first
    products_list = var1.third
    products_list_file.close()

    if ask_customer.isdigit() and 0 <= int(ask_customer) < len(products_list):
        bye()
        print("You have selected:")
        print(line)
        print(f'Product Index: {ask_customer}')
        print(f'Name: {products_list[int(ask_customer)]["Name"]}')
        print(f'Price($): {products_list[int(ask_customer)]["Price($)"]}')
        print(line)
        print()
        print("Please provide updated information for the above")
        print()
        print(line)
        while True:
            new_name= input('Please enter the updated Product name: ')
            new_price= float(input('Please enter the updated Product price: '))
            new_price = str(new_price)
            integral, fractional = (new_price).split('.')
            new_price_int = int(float(new_price))
            if new_name.isalpha(): #Checks if Name entered contains no integers.
                if str(new_price_int).isdigit() and 0 <= len(fractional) <= 2: #Checks if number entered contains no letters and is 11 didgits
                    products_list[int(ask_customer)]["Name"] = new_name or products_list[ask_customer]["Name"]
                    products_list[int(ask_customer)]["Price($)"] = new_price or products_list[ask_customer]["Price($)"] 
                    print(f'{line} \nCustomer infomation updated successfully as follows:\n')          
                    for key, value in (products_list[int(ask_customer)]).items():
                        print (f'{key}: {value}')
                    update_products_csv(products_list)
                    break
                else:
                    print(f'{line}\nPlease insert a valid Price')
            else:
                print(f'{line}\nPlease insert a valid name')
                
    else:
        print(line)
        print(f"\nError: Invalid product index.\nPlease select a value between 0 and {len(products_list)-1}")
        bye()
        update_existing_product()

def delete_product():
    print(line)
    prods() 
    user_select= input('What is the index of the order would you like to Delete?: ')
    var1 = call_products_list("r")
    
    products_list = var1.third
    if user_select.isdigit() and 0 <= int(user_select) < len(products_list):
        del products_list[int(user_select)]
        print(f'{line}\nProduct list updated successfully!\nThis is the updated list:\n{line}')
        update_products_csv(products_list)
        bye()
        prods()
    else:   
        print(f'{line}\nInvalid status index. Please Try Again!')
        bye()
        delete_product()




#================================================ ORDERS ==========================================================================================================
orders_options = ['0: Orders list', '1: Create new Order', '2: Update existing Order Status', 
                  '3: Update existing Order ', '4: Delete Order', '5: Back' ]

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
    if user_order_inp == "5": #To go back to last menu
        sleep(2)
        system('cls')
        show_full_menu()      
    elif user_order_inp == "0": #print orders -
        bye()
        print_order_list()
        another_service()
    elif user_order_inp == "1":#ADD new customer info + pr === ADD new order list----------
        bye()
        create_new_order()
    elif user_order_inp == "2":#update existing order status
        bye()
        update_existing_order_status()
        print_order_list()
        another_service()
    elif user_order_inp == "3":#update existing order
        bye()
        update_existing_order()
        print_order_list()
        another_service()
    elif user_order_inp == "4":#delete
        bye()
        delete_existing_order()
        print_order_list()
        another_service()
    else:
        print(line)
        print("That was not a valid selection, please try again.")
        bye()
        show_orders_menu()
        

  
def create_new_order():
    customer_name= input("What is the Full Name?: ")
    customer_address= input("What is the Address: ")
    customer_phone= input("What is the Telephone No.?: ")
    if type(customer_name) == str:
        if type(customer_phone) != int and len(customer_phone) != 11: 
            print("Please insert a valid telephone number consisting of 11 digits")
            create_new_order()
        else:
            print(line)
            print()
            print("These are the products currently available:")
            print()
            print(line)
            prods()
            while True:
                print()
                
                product_select = input("What are the indexes of the products you would like to purchase?\n(Please list each product index followed by a comma): ")
                nums = [int(n.replace(',', '')) for n in re.findall('[\d,]+', product_select)]
                if [c.isdigit() or c == "," for c in product_select] and [ 0 <= int(d) < len(call_products_list("r").third) for d in nums ]:
                    couriers()
                    while True:
                        courier_select = input("What is the index of the courier you would like to use?: ")
                        if courier_select.isdigit() and  0 <= int(courier_select) < len(call_couriers_list("r").third):

                            order = {
                                "Customer Name": customer_name,
                                "Customer Address": customer_address,
                                "Phone Number": customer_phone,
                                "Order Status": "Preparing",
                                "Courier": courier_select,
                                "Items": product_select
                            }
                            fields = ['Customer Name', 'Customer Address', 'Phone Number', 'Order Status',  'Courier', 'Items']

                            append_orders_list("a", order, fields)
                            print(line)
                            print()
                            print("\nOrder created successfully!\n")
                            print()
                            print(line)
                            print()
                            print("This is the updated Orders list:")
                            print_order_list()
                            another_service()
                        else:
                            print("\nThat is an invalid index. Please try again")
    

                else:
                    print("\nThat is an invalid index. Please try again")

    else:
        print("Please insert a valid name")
        create_new_order()



def update_existing_order_status():
    print_order_list()
    user_select= input('What is the index of the order would you like to change the status of?: ')
    if user_select.isdigit() and 0 <= int(user_select) < len(call_orders_list("r").third):
        bye()
        print(line)
        print("                                     ORDERS STATUSES")
        print(line)
        statuses = ["Preparing", "Ready", "Shipped", "Delivered"]
        count = 0
        for x in statuses:
            print()
            print (f'{count}: {x}')
            count = count + 1
        while True:
            
            print()
            print(line)
            print()
            new_status = input('Between 0-3, What is the new status of this order?: ')
            if new_status.isdigit() and 0 <= int(new_status) <= 3:
             # narrows it down to the specific dictionary within the car orders dict
                var = call_orders_list("r").third
                var[int(user_select)]['Order Status'] = statuses[int(new_status)]
                update_orders_csv(var)
                print()
                print(line)
                print()
                print("\nOrder Status updated successfully!\n")
                bye()
                break
            else:   
                print("\nThat is an invalid status index. Please try again")
    else:
        print("\nThat is an invalid status index. Please try again")
        update_existing_order_status()
        

def update_existing_order(): 
    print_order_list()
    user_select= input('What is the Customer index of the order would you like to change?: ')
    var = call_orders_list("r").third
    if user_select.isdigit() and 0 <= int(user_select) < len(var):
        print()
        print(line)
        print("Please provide updated information for the following")
        bye()
        while True:
            new_name= input('Please enter the updated name: ')
            new_address= input('Please enter the updated address: ')
            new_phone= input('Please enter the updated phone number: ') 
            if new_name.isalpha: #Checks if Name entered contains no integers.
                if new_phone.isdigit() and len(new_phone) == 11: #Checks if number entered contains no letters and is 11 didgits
                    
                    var[int(user_select)]["Customer Name"] = new_name or var[user_select]["Customer Name"] 
                    var[int(user_select)]["Customer Address"] = new_address or var[user_select]["Customer Address"] 
                    var[int(user_select)]["Customer Phone Number"] = new_phone or var[user_select]["Customer Phone Number"] 
                    bye()
                    print(f'{line} \nCustomer infomation updated successfully as follows!\n')          
                    for key, value in (var[int(user_select)]).items():
                        print (f'{key}: {value}')
                    print()
                    print(line)
                    update_orders_csv(var)
            
                    print("This is the updated Orders List")
                    break
                else:
                    print(f'{line}\nPlease insert a valid telephone number consisting of 11 digits')
            else:
                print(f'{line}\nPlease insert a valid name')
                
    else:
        print(f"\nInvalid order index. Please select a value between 0 and {len(var)-1}")
        update_existing_order()




def delete_existing_order():
    print_order_list()
    user_select= input('What is the index of the order would you like to Delete?: ')
    var = call_orders_list("r").third

    if user_select.isdigit() and 0 <= int(user_select) < len(var):
        del var[int(user_select)]
        print(f'{line}\n\nOrder list updated successfully!\n\nThis is the updated list:\n\n')
        update_orders_csv(var)
      
    else:   
        print(f'{line}\nInvalid status index.')
        delete_existing_order()


#=========================================== COURIERS ==========================================================================
courier_options= ['0: Courier list', '1: Create new Courier', '2: Update existing Courier', 
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
    if user_courier_inp == "0":#Print Courier list
        bye()
        couriers()
        another_service ()
    elif user_courier_inp == "1": #Create new courier
        bye()
        create_new_courier()
    elif user_courier_inp == "2": ##Update existing Courier
        bye()
        update_existing_courier()
        another_service()
    elif user_courier_inp == "3":#Delete Order
        bye()
        delete_couriers()
        another_service()
    elif user_courier_inp == "4":#Back
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

# def show_couriers_list():
#     print(line)

#     couriers()
#     while True:
#         try: 
#             print()
#             user_third_inp = int(input("Which Courier would you prefer amongst the above?\nPlease select the corresponding Courier Index: "))
#             oki = user_third_inp
#             var = call_couriers_list("r")
#             assert  oki in ((range(len((var.third)))))
#             break
#         except ValueError:
#             print("Not a Value! Please select the corresponding value for your order: ")
#             bye()
#         except AssertionError:
#             print("Not a Value within range! Please select the corresponding value for your order: ")
#             bye()
    


def create_new_courier():
    while True:
        try:
            print(line)
            
            user_input_name = string.capwords(str(input('What is the name of the Courier?: ')), sep = None)
            user_input_number = (input('What is the Telephone No.? '))
            print()
            if user_input_name.isalpha():
                if type(user_input_name) != int and len(user_input_number) != 11: 
                    print(line)
                    print()
                    print("Please insert a valid telephone number consisting of 11 digits")
                else:
                    courier = {
                            "Name": user_input_name,
                            "Phone Number": user_input_number
                        }
                    fields = ['Name', 'Phone Number']
                    append_couriers_list("a", courier, fields)
                    print(line)
    
                    print("\nNew Courier Added to list successfully!\n")
                    print(line)
                    print("This is the updated Couriers List")
                    couriers()
                    another_service()
            else:
                print("Please insert a valid name")
                
        except ValueError:
            print("Please Try Again!")
            create_new_courier()

def update_existing_courier():
    couriers()
    
    user_select= input('What is the index of the Courier you would like to change?: ')
    var = call_couriers_list("r").third
    if user_select.isdigit() and 0 <= int(user_select) < len(var):
        bye()
        print(line)
        print()
        print("Please provide updated information for the below")
        print()
        while True:
            print(line)
            new_name= input('Please enter the updated name: ')
            new_phone= input('Please enter the updated phone number: ')
            if new_name.isalpha: #Checks if Name entered contains no integers.
                if new_phone.isdigit() and len(new_phone) == 11: #Checks if number entered contains no letters and is 11 didgits
                    
                    var[int(user_select)]["Name"] = new_name or var[user_select]["Name"] 
                    var[int(user_select)]["Phone Number"] = new_phone or var[user_select]["Phone Number"] 
                    bye()
                    print(f'{line} \n\nCourier infomation updated successfully as follows!\n')
                    print(line)
                    print()          
                    for key, value in (var[int(user_select)]).items():
                        
                        print (f'{key}: {value}')
                    update_couriers_csv(var)
                    print()
                    print(line)
                    print()
                    print("The updated List is as follows:")
                    print()
                    bye()
                    couriers()
                    break
                else:
                    print(line)
                    print()
                    print(f'{line}\nPlease insert a valid telephone number consisting of 11 digits')
            else:
                print(line)
                print()
                print(f'{line}\nPlease insert a valid name')
                
    else:
        print(line)
        print()
        print(f"\nInvalid order index. Please select a value between 0 and {len(var)-1}")
        print()
        print(line)
        update_existing_courier()


def delete_couriers():
    
    couriers()
    user_select= input('What is the index of the Courier you would like to delete?: ')
    var = call_couriers_list("r").third
    if user_select.isdigit() and 0 <= int(user_select) < len(var):
        del var[int(user_select)]
        print()
        print(f'{line}\nOrder list updated successfully!\nThis is the updated list:\n')
        print()
        bye()
        update_couriers_csv(var)
        couriers()
    else:   
        print(f'{line}\nInvalid status index.')
        bye()
        delete_couriers()
        
   
# ==================================================================================================================================================================================


#                           oi YOU! Yes, YOU!
# THE FUN STARTS HERE!!! (only 3 lines.. I know, but don't be deceived. It's smoll but mighty!)
print(line)
print()
print('                        Welcome to Dunkin Donuts! ^_^')
print()
show_main_menu()


























# ==================================================================================================================================================================================
# IF NEEDED! FOR REFERENCE LATER(pay no attention to these)

# customer_orders = [
# {
#     'Customer Name': 'Bob',
#     'Customer Address': '12 Everglade terrace, London, SW18 1UE',
#     'Customer Phone Number' : '020889874576',
#     'Order Status': 'Ready',
#     'Courier': '1',
# },
# {
#     'Customer Name': 'Carl',
#     'Customer Address': '10 Mill HIll Road, London, W3 68E',
#     'Customer Phone Number' : '02083357545',
#     'Order Status': 'Ready',
#     'Courier': '1',
# },
# {
#     'Customer Name': 'Ran',
#     'Customer Address': '11 Everglade terrace, London, SW18 1UE',
#     'Customer Phone Number' : '02088932432 ',
#     'Order Status': 'Ready',
#     'Courier': '1',
# },
# {
#     'Customer Name': 'Tom',
#     'Customer Address': 'Flat 1, Workcast Avenue, London, NW18 0KE',
#     'Customer Phone Number' : '02088934256',
#     'Order Status': 'Ready',
#     'Courier': '1',
# }
#   ]
# with open('orders.json', 'w') as fp:
#   json.dump( customer_orders , fp, indent=4, separators=(',',': '))

# product_list = [
# {
#    "Name": 'Strawberry',
#    "Price($)": 1.20
# }, 
# { 
#    "Name": 'Chocolate',
#    "Price($)": 1.40
# },
# {
#     "Name": 'Raspberry',
#     "Price($)": 1.40
# }, 
# { 
#     "Name": 'Vanilla',
#     "Price($)": 1.40
# },
# {
#     "Name":  'Glazed',
#     "Price($)": 1.5
# ]

# # myFile = open('products.csv', 'w')
# # writer = csv.writer(myFile)
# # writer.writerow(['Name', 'Price'])
# # for dictionary in product_list:
# #     writer.writerow(dictionary.values())
# # myFile.close()



# customer_orders = [
# {
#     'Customer Name': 'Bob',
#     'Customer Address': '12 Everglade terrace, London, SW18 1UE',
#     'Customer Phone Number' : '020889874576',
#     'Order Status': 'Ready',
#     'Courier': '4',
#     'Items': '2',
# },
# {
#     'Customer Name': 'Carl',
#     'Customer Address': '10 Mill HIll Road, London, W3 68E',
#     'Customer Phone Number' : '02083357545',
#     'Order Status': 'Ready',
#     'Courier': '1',
#     'Items': '1, 3',
# },
# {
#     'Customer Name': 'Ran',
#     'Customer Address': '11 Everglade terrace, London, SW18 1UE',
#     'Customer Phone Number' : '02088932432 ',
#     'Order Status': 'Ready',
#     'Courier': '1',
#     'Items': '1, 2, 3', 
# },
# {
#     'Customer Name': 'Tom',
#     'Customer Address': 'Flat 1, Workcast Avenue, London, NW18 0KE',
#     'Customer Phone Number' : '02088934256',
#     'Order Status': 'Ready',
#     'Courier': '3',
#     'Items': '2',
# }
#   ]

# # myFile = open('orders.csv', 'w')
# # writer = csv.writer(myFile)
# # writer.writerow(['Customer Name', 'Customer Address', 'Customer Phone Number', 'Order Status',  'Courier', 'Items'])
# # for dictionary in customer_orders:
# #     writer.writerow(dictionary.values())
# # myFile.close()


# couriers_list = [
# {
#    "Name": 'Barbe',
#    "Phone Number": '07977745891'
# }, 
# { 
#     "Name": 'Karl',
#     "Phone Number": '07977567891'
# },
# {
#    "Name": 'Toma',
#    "Phone Number": '07977789091'
# }, 
# { 
#    "Name": 'Paul',
#    "Phone Number": '07437745891'
# },
# {
#    "Name": 'Ken',
#    "Phone Number": '07967845891'
# }
# ]
# myFile = open('couriers.csv', 'w')
# writer = csv.writer(myFile)
# writer.writerow(["Name", "Phone Number"])
# for dictionary in couriers_list:
#     writer.writerow(dictionary.values())
# myFile.close()