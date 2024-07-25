import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Establish connection to the MySQL server
        cnx = mysql.connector.connect(
            user='root',  # Replace with your MySQL username
            password='Abdou@324E.',  # Replace with your MySQL password
            host='127.0.0.1',  # Adjust if MySQL server is on a different host
            port='3306'  # Ensure this is correct
        )
        cursor = cnx.cursor()
        
        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        # Print success message
        print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    except Exception as e:
        print(f"Error: {e}")
    else:
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    create_database()
