from databricks import sql
import os


with sql.connect(server_hostname = "adb-5595195760454296.16.azuredatabricks.net",
                 http_path       = "sql/protocolv1/o/5595195760454296/0201-101611-o3q4m3vr",
                 access_token    = "dapif04aab29bb41fcfb0b00480e0e679c07") as connection:

  with connection.cursor() as cursor:
 
    print("Now inserting data")
    cursor.execute("INSERT INTO STUDENTS VALUES('Palash',22)")
    cursor.execute("SELECT * FROM STUDENTS LIMIT 10")
    result = cursor.fetchall()

    for row in result:
      print(row)