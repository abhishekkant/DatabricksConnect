import mysql.connector


# import logging

# # configure the root logger to write to a file and console
# logging.basicConfig(filename='example.log', level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s: %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S')
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# console.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
# logging.getLogger().addHandler(console)


# log messages at different levels
# logging.info('Starting to establish connection to MariaDB')


# establish a connection to the MySQL server

cnx = mysql.connector.connect(user='root', password='example',
                              host='127.0.0.1', database='pythonlearning', port=3306)


# create a cursor object to execute SQL queries
cursor = cnx.cursor()

# execute a simple SELECT query
query = "SELECT * FROM interns"
cursor.execute(query)

# fetch all rows of the query result
result = cursor.fetchall()

# print the result
for row in result:
    print(row)

# close the cursor and database connection
cursor.close()
cnx.close()


# logging.debug('This is a debug message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
