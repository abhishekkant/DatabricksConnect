from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    # establish a connection to the MySQL server
    cnx = mysql.connector.connect(user='root', password='example',
                                  host='127.0.0.1', database='pythonlearning', port=3306)

    # create a cursor object to execute SQL queries
    cursor = cnx.cursor()

    # execute a SELECT query to fetch all rows from a table
    query = "SELECT * FROM interns"
    cursor.execute(query)

    # fetch all rows of the query result
    result = cursor.fetchall()

    # close the cursor and database connection
    cursor.close()
    cnx.close()

    # pass the result to the template and render it
    return render_template('index.html', rows=result)

if __name__ == '__main__':
    app.run(debug=True)
