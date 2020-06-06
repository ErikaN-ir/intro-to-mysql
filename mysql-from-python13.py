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
        names = ['jim', 'bob']
        cursor.execute("DELETE FROM FRIENDS WHERE name in (%s,%s)", names)
        connection.commit()
finally:
    # Close the connnection to sql
    connection.close()