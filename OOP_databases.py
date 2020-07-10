# Importing module for database methods
import pyodbc

# Create class
class Database:

    # Intiliasing class
    def __init__(self, connection_string):
        self.connection_string = connection_string

    # Create function to intialise connection
    def create_connection(self):
        try:
            with pyodbc.connect(self.connection_string, timeout=20) as self.connection:
                print("Connection worked")
        except:
            print("Connection timed out")
        raise Exception as e:
            print("You got this error", e)
        return self.connection

    # Create function to intialise cursor
    def create_cursor(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    # Sends user to functions below. Uses value error and to let user know what to do
    def fetch_information(self):
        # Query result getting all data from products
        query_result = self.cursor.execute("select * from Products")
        method_called = input("Would you like to fetch all, many or one?\nType all, many or one for the respective option \n")
        # If loop to check user input
        if method_called == "all":
            self.fetch_all(query_result)
        elif method_called == "many":
            rows_called = int(input("How many rows would you like?\n"))
            self.fetch_many(query_result, rows_called)
        elif method_called == "one":
            self.fetch_one(query_result)
        else:
            pass


    # Create function to fetch all
    def fetch_all(self, query):
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    # Create function to fetch many
    def fetch_many(self, query, rows_called):
        rows = self.cursor.fetchmany(rows_called)
        for row in rows:
            print(row)

    # Create function to fetch one
    def fetch_one(self, query):
        rows = self.cursor.fetchone()
        for row in rows:
            print(row)

    # Assignment: Calculate the average unit price of all the products
    def average_price2(self):
        self.cursor.execute("SELECT AVG(UnitPrice) from Products")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)


    def average_price(self):
        self.cursor.execute("select * from Products")
        rows = self.cursor.fetchall()
        row_count = 0
        unit_price_sum = 0.00
        for row in rows:
            row_count += 1
            unit_price_sum = unit_price_sum + float(row.UnitPrice)
        average_unit_price = float(unit_price_sum) / float(row_count)
        print("The average unit price is:", average_unit_price, "pounds")