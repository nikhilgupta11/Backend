#!/usr/bin/python3
import pymysql
import cgi,cgitb


cgitb.enable()
form = cgi.FieldStorage()

db = pymysql.connect(host="localhost",user="root",password="",database="student" )

cursor = db.cursor()

cursor.execute("SELECT * from new")
data = cursor.fetchall()


print ("Content-type: text/html\r\n\r\n")
print ("<html>")

print ("<head>")
print ("<title>Admin Panel</title>")
print("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3' crossorigin='anonymous'>")
print ("</head>")

print ("<body>")

print("<nav class='navbar navbar-dark bg-dark'>")


print("</nav>")

print(" <table class='table'>")

print("<thead>")
print ("<tr>")
print("<th scope='col'>id</th>")
print("<th scope='col'>Name</th>")      
print("<th scope='col'>Address</th>")     
print("<th scope='col'>Mobile</th>")    
print("<th scope='col'>Email</th>")     
# print("<th scope='col'>Password</th>") 
print("<th scope='col'>Update</th>")
print("<th scope='col'>Delete</th>")    
print( "</tr>")
print("</thead>")

print("<tbody>")
for row in data:    
    id = row[0]
    name = row[1]
    Address = row[2]
    Mobile = row[3]
    Email = row[4]
    # Password = row[5]
    print("<tr><td>%s</td>" %(id))
    print("<td>%s</td>" %(name))
    print("<td>%s</td>" %(Address))
    print("<td>%s</td>" %(Mobile))
    print("<td>%s</td>" %(Email))
    # print("<td>%s</td></tr>" %(Password))
    # print("<td> <a href='update.py'>Update</a> </td>")
    # print("<td><a href='delete.py'>Delete</a> </td></tr>")
    # print("<td><input type='button' name='Update' 'onclick='update.py';'></td>")
    # print("<td><input type='button' name='Delete' 'onclick='delete.py';'></td></tr>")
    # print("<td><button type='button' class='btn btn-primary'><a href='update.py' ?id=%s>Update</a></button></td>" %id)
    # print("<td><button type='button' class='btn btn-primary'><a href='delete.py' ?id=%s>Delete</a></button></td></tr>" %id)
    print("<td><a href='update.py?id=%s'>Update</a></td>"%id)
    print("<td><a href='delete.py?id=%s'>Delete</a></td>"%id)
print ("</tbody>")
print("</table>")  
# print("<script src='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js' integrity='sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p' crossorigin='anonymous'></script>")
print ("</body>")
print ("</html>")

db.close() 
