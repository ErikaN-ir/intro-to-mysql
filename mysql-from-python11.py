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
        rows = cursor.executemany("DELETE FROM FRIENDS WHERE name = %s;", ['Bob', 'Jim'])
        connection.commit()
finally:
    # Close the connnection to sql
    connection.close()