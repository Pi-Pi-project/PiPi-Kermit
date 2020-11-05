import pymysql
import pandas as pd
from DB_connect_setting import DB

cursor = DB.cursor(pymysql.cursors.DictCursor)
sql = "SELECT *" \
      "FROM user_skillset;"

cursor.execute(sql)
result = cursor.fetchall()
print(result)

result = pd.DataFrame(result)
print(result)

DB.close()