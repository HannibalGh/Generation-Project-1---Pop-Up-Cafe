import mysql.connector

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="test"  # Update this if needed
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
