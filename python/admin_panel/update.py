#!/usr/bin/python3
import pymysql
import cgi,cgitb

cgitb.enable() 

form = cgi.FieldStorage()
print ("Content-type: text/html\r\n\r\n")

db = pymysql.connect(host="localhost",user="root",password="",database="student")
cursor=db.cursor()

sid = form.getvalue('id')



id = form.getvalue(id)
name = form.getvalue(name)
Address = form.getvalue(Address)
Mobile = form.getvalue(Mobile)
Email = form.getvalue(Email)

try:
	cursor.execute("update new set name='%s',Address='%s',Mobile='%s',Email='%s' where id=%s" %(name,Address,Mobile,Email,id))
	db.commit()
	print("Data Updated")
    # print("<button type='button' class='btn btn-primary'><a href='update.py'>Update</a></button>")
    # print(" <input type='submit' name='Submit'>")
    
except:
    db.rollback()
    print("error in updating")

# print ("</body>")
# print ("</html>")

db.close()