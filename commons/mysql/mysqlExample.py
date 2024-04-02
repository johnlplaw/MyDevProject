import mysqlHelper

# # Create connection
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="myroot"
# )
# print(mydb)

# # To create a new database
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE myresearch")

# To check the cursor
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

mydb = mysqlHelper.get_mysql_conn()
print(mydb)