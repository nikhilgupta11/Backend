#!/usr/bin/python3
import pymysql
import cgi,cgitb

cgitb.enable() 

form = cgi.FieldStorage()
print ("Content-type: text/html\r\n\r\n")

db = pymysql.connect(host="localhost",user="root",password="",database="student")
cursor=db.cursor()

sid = form.getvalue('id')

print ("<html>")
print ("<head>")
print ("<title>Delete</title>")
print ("</head>")
print ("<body>")


try:
    # execute SQL query using execute() method.
    cursor.execute("delete from new where id=%s" %(sid))
    # Commit your changes in the database
    db.commit()
    print("Data Deleted")

except:
    # Rollback in case there is any error
    db.rollback()
    print("error in Deleting")

print ("</body>")
print ("</html>")


db.close()