import os
import datetime
import pymysql
#Get username from workspace

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        FRIENDS(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not eror) if the table already exists      
finally:
    # Close the connnection to sql
    connection.close()