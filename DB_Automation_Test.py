import pymysql
import pandas as pd
import numpy as np
from db_connect_setting import DB

"""
==========Get user skillset==========
select user.email as 'email', user_skillset.skill as 'user_skill'
from user, user_skillset
where user.email='a@gmail.com' and user.email=user_skillset.user_email;

==========Get user search log==========
select user.email as 'email', user_search_log.log as 'search_log'
from user, user_search_log
where user.email='a@gmail.com' and user.email=user_search_log.user_email;

==========Get user view log==========
select user.email as 'email', user_view_log.log as 'view_log'
from user, user_view_log
where user.email='a@gmail.com' and user.email=user_view_log.user_email;
"""

def _sql_set(email):
    sql = "select distinct user_skillset.user_email, user_skillset.skill, user_search_log.log, user_view_log.log from user_skillset, user_search_log, user_view_log where user_skillset.user_email="\
          + "'" + str(email) + "' " + "and user_skillset.user_email=user_search_log.user_email and user_skillset.user_email=user_view_log.user_email;"

    return sql

cursor = DB.cursor(pymysql.cursors.DictCursor)
cursor.execute(_sql_set("a@gmail.com"))
result = cursor.fetchall()

print("Non Pandas")
for i in result:
    print(i)

print("\n=====================================================\n")

pd_result = pd.DataFrame(result)
print("Pandas")
print(pd_result)

print("\n=====================================================\n")
print("Pandas Test")
print(pd_result["skill"])
print(list(pd_result["skill"]))
print(set(list(pd_result["skill"])))

DB.close()