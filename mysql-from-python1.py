import os
import pymysql
#Get username from workspace

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    # Close the connnection to sql
    connection.close()