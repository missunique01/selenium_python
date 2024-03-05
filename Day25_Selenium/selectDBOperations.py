#select

select_query = "select * from student;"
import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", port=3306,user="root",passwd = "Nazma786@", database = "pythonseleniumdb")
    curs = con.cursor()
    curs.execute(select_query)

    # print(curs)  #MySQLCursor: select * from student;
    #To print multiple records in the table
    for row in curs:
        print(row[0],row[1], row[2])
    con.close()
except:
    print("Connection Unsuccessfull")

print("FInished")