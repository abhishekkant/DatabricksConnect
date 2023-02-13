import pyodbc

# Replace YOUR_DSN_NAME with the name of your DSN
DSN_NAME = "YOUR_DSN_NAME"

# Replace YOUR_SQL_QUERY with the SQL query you want to execute
SQL_QUERY = "YOUR_SQL_QUERY"

# Connect to the DSN
conn = pyodbc.connect("DSN=" + DSN_NAME)

# Execute the SQL query and store the results
cursor = conn.cursor()
cursor.execute(SQL_QUERY)
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
