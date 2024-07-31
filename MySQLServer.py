import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        cnx = mysql.connector.connect(
            user='your_username',       
            password='your_password',   
            host='localhost'               
        )
        cursor = cnx.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

if __name__ == "__main__":
    create_database()
def create_tables_and_insert_data():
    try:

        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='localhost',
            database='alx_book_store'
        )
        cursor = cnx.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            published_date DATE
        )
        """
        cursor.execute(create_table_query)

        insert_data_query = """
        INSERT INTO books (title, author, published_date)
        VALUES (%s, %s, %s)
        """
        book_data = (
            ("Book Title 1", "Author 1", "2024-01-01"),
            ("Book Title 2", "Author 2", "2023-07-31"),
            ("Book Title 3", "Author 3", "2022-05-15")
        )
        cursor.executemany(insert_data_query, book_data)
        cnx.commit()

        print("Table created and data inserted successfully!")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

if __name__ == "__main__":
    create_tables_and_insert_data()
def query_data():
    try:
        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='localhost',
            database='alx_book_store'
        )
        cursor = cnx.cursor()

        query = "SELECT * FROM books"
        cursor.execute(query)

        for (id, title, author, published_date) in cursor:
            print(f"ID: {id}, Title: {title}, Author: {author}, Published Date: {published_date}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

if __name__ == "__main__":
    query_data()
def update_and_delete_data():
    try:
        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='localhost',
            database='alx_book_store'
        )
        cursor = cnx.cursor()

        update_query = "UPDATE books SET author = %s WHERE title = %s"
        cursor.execute(update_query, ("New Author", "Book Title 1"))
        cnx.commit()

        delete_query = "DELETE FROM books WHERE title = %s"
        cursor.execute(delete_query, ("Book Title 2",))
        cnx.commit()

        print("Data updated and deleted successfully!")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

if __name__ == "__main__":
    update_and_delete_data()
import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='localhost'
        )
        cursor = cnx.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

def create_tables_and_insert_data():
    try:
        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='localhost',
            database='alx_book_store'
        )
        cursor = cnx.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            published_date DATE
        )
        """
        cursor.execute(create_table_query)

        insert_data_query = """
        INSERT INTO books (title, author, published_date)
        VALUES (%s, %s, %s)
        """
        book_data = (
            ("Book Title 1", "Author 1", "2024-01-01"),
            ("Book Title 2", "Author 2", "2023-07-31"),
            ("Book Title 3", "Author 3", "2022-05-15")
        )
        cursor.executemany(insert_data_query, book_data)
        cnx.commit()

        print("Table created and data inserted successfully!")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

def query_data():
    try:
        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='localhost',
            database='alx_book_store'
        )
        cursor = cnx.cursor()

        query = "SELECT * FROM books"
        cursor.execute(query)

        for (id, title, author, published_date) in cursor:
            print(f"ID: {id}, Title: {title}, Author: {author}, Published Date: {published_date}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

def update_and_delete_data():
    try:
        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='localhost',
            database='alx_book_store'
        )
        cursor = cnx.cursor()

        update_query = "UPDATE books SET author = %s WHERE title = %s"
        cursor.execute(update_query, ("New Author", "Book Title 1"))
        cnx.commit()

        delete_query = "DELETE FROM books WHERE title = %s"
        cursor.execute(delete_query, ("Book Title 2",))
        cnx.commit()

        print("Data updated and deleted successfully!")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

if __name__ == "__main__":
    main() 