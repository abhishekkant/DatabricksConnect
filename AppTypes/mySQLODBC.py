import pyodbc

# Replace the values in angle brackets with your MySQL server's details
server = '127.0.0.1'
database = 'pythonlearning'
username = 'root'
password = 'example'

# Set up the ODBC connection string
conn_str = f"DRIVER={{MySQL ODBC 8.0 Driver}}; SERVER={server}; DATABASE={database}; UID={username}; PWD={password}"

# Connect to the database using pyodbc
cnxn = pyodbc.connect(conn_str)

# Use the connection to execute SQL commands
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM interns')

# Fetch the results and print them
for row in cursor.fetchall():
    print(row)

# Close the connection when finished
cnxn.close()
