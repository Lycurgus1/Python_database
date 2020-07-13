# Database theory
**Creating a connection**
- Connection string. This is used to connect to a server.
```python
connection_string = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
```
- Hiding log-in details. To this we use enviromental variables, then call these.
```python
server = os.environ.get('db_server')
database = os.environ.get('db_database')
username = os.environ.get('db_username')
password = os.environ.get('db_password')
```
- Creating a connection
    - To do this it is best to use the with command
    - Otherwise a connection must be closed after opening
    - This can also be contained in a try except loop to make sure it connects!
```python
with pyodbc.connect(self.connection_string, timeout=20) as self.connection          
```
 - Creating a cursor. This creates the cursor then returns it to the class
 ```python
    def create_cursor(self):
        self.cursor = self.connection.cursor()
        return self.cursor
```
- Fetchall. This fetches all rows from a SQL query
```python
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
```
- Fetch many. This fetches multiple role based on a specified value
```python
        rows = self.cursor.fetchmany(2)
        for row in rows:
            print(row)
```
- Fetch one. This fetches on row
```python
        rows = self.cursor.fetchone()
        for row in rows:
            print(row)
```