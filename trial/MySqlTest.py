import commons.mysql.mysqlHelper as sqlHelper

conn = sqlHelper.get_mysql_conn()

mycursor = conn.cursor()

sql = "INSERT INTO mydataset (label, oritxt, cleannedtxt) VALUES (%s, %s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

conn.commit()

print(mycursor.rowcount, "record inserted.")