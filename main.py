from OOP_databases import Database

# Defining database username etc variables
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Creating connections string object with variables
connection_string = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=' + database +';UID='+ username +';PWD='+ password)


# Calling functions
# Creating class instance
obj1 = Database(connection_string)
obj1.create_connection()
obj1.create_cursor()
# obj1.fetch_information()
obj1.average_price2()