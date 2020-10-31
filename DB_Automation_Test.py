import pymysql
import pandas as pd
from db_connect_setting import DB

"""
TEST SQL Query
select user_skillset.user_email, user_skillset.skill, user_search_log.log, user_view_log.log
from user_skillset, user_search_log, user_view_log
where user_skillset.user_email='a@gmail.com' and user_skillset.user_email=user_search_log.user_email and user_skillset.user_email=user_view_log.user_email;
"""

def _sql_set(email):
    sql = "select distinct user_skillset.user_email, user_skillset.skill, user_search_log.log, user_view_log.log from user_skillset, user_search_log, user_view_log where user_skillset.user_email="\
          + "'" + str(email) + "' " + "and user_skillset.user_email=user_search_log.user_email and user_skillset.user_email=user_view_log.user_email;"

    return sql

cursor = DB.cursor(pymysql.cursors.DictCursor)
cursor.execute(_sql_set("a@gmail.com"))
result = cursor.fetchall()

for i in result:
    print(i)

print("\n=====================================================\n")

pd_result = pd.DataFrame(result)
print(result)

DB.close()