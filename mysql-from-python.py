import os
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environmet)
username = os.getenv('C9_USER')


# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')


try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        # Execute the sql command above
        cursor.execute(sql)
        # Fetch all is just getting the data back
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()