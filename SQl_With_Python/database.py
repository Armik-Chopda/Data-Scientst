import mysql.connector
mySQL=mysql.connector.connect(host='localhost',password='Armik@1411',user='root')

if mySQL.is_connected():
    print("Your connection is successful")