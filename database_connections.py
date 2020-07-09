# Importing module for database
# Library to help connect to database
import pyodbc

# Goal is to establish connection & read data from database to the python console

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'


# Specifying the ODBC driver, server name, database, etc. directly
# ODBC = api for connecting to microsoft applications and servers. Open database connection
# Differiantes from documentation slightly
connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password

# Trying to connect with database string. If not able to connect it times out in 5 seconds
try:
    with pyodbc.connect(connection_string, timeout = 20) as connection:
        print("connection did not time out")
except:
    print("Connection timed out")
else:
    # Get cursor from connection  to execute the codethrough
    # Using cursor.fetch to iterate through rows of data
    cursor = connection.cursor()
    print(connection)
    print(cursor)


# # Using a DSN, but providing a password as well
# cnxn = pyodbc.connect('DSN=test;PWD=password')
#
# # Create a cursor from the connection
# cursor = cnxn.cursor()

# import pyodbc
# # server = 'databases2.spartaglobal.academy'
# # database = 'Northwind'
# # username = 'SA'
# # password = 'Passw0rd2018'
# #
# # import pyodbc
# server = 'databases2.spartaglobal.academy'
# #databases2.spartaglobal.academy
# database = 'Northwind'
# username = 'SA'
# password = 'Passw0rd2018'
# connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = connections.cursor()
# print(connections)
# print(cursor)