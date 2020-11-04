import pymysql
import pandas as pd
from db_connect_setting import DB

def _user_skill(email):
    sql_query = "select user.email as 'email', user_skillset.skill as 'user_skill' from user, user_skillset where user.email=" \
                + "'" + str(email) + "' " + "and user.email=user_skillset.user_email;"

    skill_cursor = DB.cursor(pymysql.cursors.DictCursor)
    skill_cursor.execute(sql_query)
    skill_result = skill_cursor.fetchall()

    return pd.DataFrame(skill_result)