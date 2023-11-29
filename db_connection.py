import mysql.connector

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='myStore',
            user='root',
            password=''
        )
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    return connection