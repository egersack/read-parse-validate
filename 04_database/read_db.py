import mysql.connector

cnx = mysql.connector.connect(user='root',
    password = 'Ella050503!!',
    host = '127.0.0.1',
    database = 'Farm',
    auth_plugin = 'mysql_native_password')

# query
cursor = cnx.curser()
query = ('SELECT * FROM Customers')
cursor.execute(query)

# loop through data
for row in cursor.fetchall():
    print(row)

# clean up
cursor.close()
cnx.close()