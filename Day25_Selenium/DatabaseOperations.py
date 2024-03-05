#insert, Update, Delete

insert_query = "insert into student values(103,'Abdul','Europe')"
update_query = "update student set sname = 'Hameed' where sid =103"
delete_query = "delete from student where sid = 103 "
import mysql.connector

#Establishing the connection to MYSQL DB
try:
    con = mysql.connector.connect(host="localhost", port=3306,user="root",passwd = "Nazma786@", database = "pythonseleniumdb")
    curs = con.cursor()  # Create a cursor
    # curs.execute("insert into student values(103,'Abdul','Europe')") #Execute the query using cursor
    curs.execute(delete_query) #Execute the query using cursor
    con.commit()  #Commit transaction
    con.close()
except:
    print("Connection Unsuccessful")
print("Finished")

