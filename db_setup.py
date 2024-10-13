import csv
from db_connection import connect_db

def create_tables():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()

        # Create table queries
        product_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        );
        """

        courier_table = """
        CREATE TABLE IF NOT EXISTS couriers (
            id INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone_number VARCHAR(15) NOT NULL
        );
        """
        
        orders_table = """
        CREATE TABLE IF NOT EXISTS orders (
            id INT PRIMARY KEY,
            customer_name VARCHAR(255) NOT NULL,
            customer_address VARCHAR(255) NOT NULL,
            customer_phone_number VARCHAR(15) NOT NULL,
            order_status VARCHAR(255),
            courier INT,
            items TEXT,
            FOREIGN KEY (courier) REFERENCES couriers(id)
        );
        """

        # Execute the table creation queries
        cursor.execute(product_table)
        cursor.execute(courier_table)
        cursor.execute(orders_table)

        connection.commit()
        print("Tables created successfully.")
        
        # Load data from CSV files
        load_data_from_csv(connection)
        
        cursor.close()
        connection.close()

def load_data_from_csv(connection):
    cursor = connection.cursor()

    # Load data into the products table from products.csv
    with open('products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader, start=1):
            # Check if the product with the current ID already exists
            cursor.execute("""SELECT id FROM products WHERE id = %s""", (index,))
            product = cursor.fetchone()

            if product is None:
                # Insert new product if the ID does not exist
                cursor.execute("""INSERT INTO products (id, name, price) VALUES (%s, %s, %s)""",
                               (index, row['Name'], row['Price($)']))

    # Load data into the couriers table from couriers.csv
    with open('couriers.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader, start=1):
            # Check if the courier with the current ID already exists
            cursor.execute("""SELECT id FROM couriers WHERE id = %s""", (index,))
            courier = cursor.fetchone()

            if courier is None:
                # Insert new courier if the ID does not exist
                cursor.execute("""INSERT INTO couriers (id, name, phone_number) VALUES (%s, %s, %s)""",
                               (index, row['Name'], row['Phone Number']))

    # Load data into the orders table from orders.csv
    with open('orders.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader, start=1):
            # Check if the order with the current ID already exists
            cursor.execute("""SELECT id FROM orders WHERE id = %s""", (index,))
            order = cursor.fetchone()

            if order is None:
                # Insert new order if the ID does not exist
                cursor.execute("""INSERT INTO orders (id, customer_name, customer_address, customer_phone_number, order_status, courier, items) VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                               (index, row['Customer Name'], row['Customer Address'], row['Customer Phone Number'], row['Order Status'], row['Courier'], row['Items']))

    connection.commit()
    print("Data loaded successfully.")
    cursor.close()
