#!/usr/bin/env python3
"""
MySQLServer.py
Script to create the database 'alx_book_store' in MySQL.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL Server (update host, user, password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password_here"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection closed.")  # optional if you want this message

if __name__ == "__main__":
    create_database()