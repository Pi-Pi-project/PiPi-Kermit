import pandas as pd
import pymysql
from DB_connect_setting import DB

cursor = DB.cursor(pymysql.cursors.DictCursor)

def  _user_skill(email):
    sql_query = "select user.email as 'email', user_skillset.skill as 'user_skill' from user, user_skillset where user.email=" \
                + "'" + str(email) + "' " + "and user.email=user_skillset.user_email"

    cursor.execute(sql_query)
    user_skill = pd.DataFrame(cursor.fetchall())

    return user_skill

def _user_search_log(email):
    sql_query = "select user.email as 'email', user_search_log.log as 'search_log' from user, user_search_log where user.email=" \
                + "'" + str(email) + "' " + "and user.email=user_search_log.user_email"

    cursor.execute(sql_query)
    user_search_log = pd.DataFrame(cursor.fetchall())

    return user_search_log

def _user_view_log(email):
    sql_query = "select user.email as 'email', post.id as 'post_id', post.title as 'title', post.content as 'post_content', user_view_log.log as 'view_log' from user, post, user_view_log where user.email=" \
                + "'" + str(email) + "' " + "and user.email=user_view_log.user_email"

    cursor.execute(sql_query)
    user_view_log = pd.DataFrame(cursor.fetchall())

    return user_view_log

# try:
#     cursor.execute(_user_skill(email))
#     user_skill = pd.DataFrame(cursor.fetchall())
#
#     cursor.execute(_user_search_log(email))
#     user_search_log = pd.DataFrame(cursor.fetchall())
#
#     cursor.execute(_user_view_log(email))
#     user_view_log = pd.DataFrame(cursor.fetchall())

# finally:
#     DB.close()

# Test
# print(user_skill)
# print(user_search_log)
# print(user_view_log)