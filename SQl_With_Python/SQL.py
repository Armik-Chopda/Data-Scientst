import mysql.connector
mySQL=mysql.connector.connect(host='localhost',password='Armik@1411',user='root')

mycursor=mySQL.cursor()

if mySQL.is_connected():
    print(mySQL.server_host)
    mycursor.execute("SHOW DATABASES")
    
    for i in mycursor:
        print(i)
    
    print("Connected")
mycursor.execute("CREATE TABLE if not exists armik.data(id INT NOT NULL,name VARCHAR(30),email VARCHAR(30))")

mycursor.execute("insert into armik.data values(1,'armik','armikchopda@gmail.com')")
mySQL.commit()
mycursor.execute("select * from armik.data")
for j in mycursor.fetchall():
    print(j)


mySQL.close()