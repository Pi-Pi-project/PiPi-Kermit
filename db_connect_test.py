import pymysql
from db_connect_setting import DB

cursor = DB.cursor(pymysql.cursors.DictCursor)
sql = "select * from user where email='a@gmail.com';"

cursor.execute(sql)
result = cursor.fetchall()
print(result)