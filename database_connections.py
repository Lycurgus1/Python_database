import os
# Importing module for database
# Library to help connect to database
import pyodbc

# Goal is to establish connection & read data from database to the python console

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# # Specifying the ODBC driver, server name, database, etc. directly
# # ODBC = api for connecting to microsoft applications and servers. Open database connection

# # Testing without using Try loop, due to erros
# connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=' + database +';UID='+ username +';PWD='+ password)
# cursor = connections.cursor()
# print(connections)
# print(cursor)

# Differiantes from documentation slightly
connection_string = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=' + database +';UID='+ username +';PWD='+ password)

# Trying to connect with database string. If not able to connect it times out in 5 seconds
# def connection_loop(connection):
try:
    with pyodbc.connect(connection_string, timeout = 20) as connection:
        print("connection did not time out")
except:
    print("Connection timed out")
else:
    # Get cursor from connection  to execute the codethrough
    # Using cursor.fetch to iterate through rows of data
    cursor = connection.cursor()
    # print(connection)
    # print(cursor)#
#
# connection_loop(connection_string)

# # Connecting to server
# cnxn = pyodbc.connect(connection_string)
# # Creating cursor
# cursor = cnxn.cursor()
# Executing SQL command
query_result = cursor.execute("select * from Customers ")
print(query_result)

# Fetching all rows
rows = cursor.fetchall()

# Fetching multiple rows
# rows = cursor.fetchmany(2)

# # Fetching one row
# rows = cursor.fetchone()

# # Print methods
# # Printing rows using for loop
# for row in rows:
#     print(row)

# # Printing row in rows, getting row info from column1 and contact name category for each row
# for row in rows:
#     print("Column1 :", row[0])
#     print("ContactName :", row.ContactName)

# # Printing 1st row in table
# print(rows[0])
#
# # Printing value for column name. Can only do so if printing one row
# print(rows.CompanyName)






