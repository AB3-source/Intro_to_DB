#!/usr/bin/python3
"""
MySQLServer.py
Creates the database alx_book_store in MySQL server.
"""

import mysql.connector

try:
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"  # <-- replace with your actual MySQL root password
    )
    cursor = conn.cursor()

    # Create database if it does not exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Ensure DB connection closes
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()