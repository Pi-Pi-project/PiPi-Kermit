import pymysql
import pandas as pd
from DB_connect_setting import DB

def _user_search_log(email):
    sql_query = "select user.email as 'email', user_search_log.log as 'search_log' from user, user_search_log" \
                + "'" + str(email) + "' " + "and user.email=user_search_log.user_email;"

    search_cursor = DB.cursor(pymysql.cursors.DictCursor)
    search_cursor.execute(sql_query)
    search_result = search_cursor.fetchall()

    return pd.DataFrame(search_result)