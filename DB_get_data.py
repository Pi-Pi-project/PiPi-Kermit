import pandas as pd
import pymysql
from DB_connect_setting import DB

cursor = DB.cursor(pymysql.cursors.DictCursor)

def  _user_skill(email):
    sql_query = "select user.email as 'email', user_skillset.skill as 'user_skill'" \
                "from user, user_skillset where user.email=" \
                + "'" + str(email) + "' " + "and user.email=user_skillset.user_email"

    cursor.execute(sql_query)
    user_skill = pd.DataFrame(cursor.fetchall())

    return user_skill

def _user_search_log(email):
    sql_query = "select user.email as 'email', user_search_log.log as 'search_log'" \
                "from user, user_search_log where user.email=" \
                + "'" + str(email) + "' " + "and user.email=user_search_log.user_email"

    cursor.execute(sql_query)
    user_search_log = pd.DataFrame(cursor.fetchall())

    return user_search_log

def _user_view_log(email):
    sql_query = "select user.email as 'email', post.id as 'id', post.title as 'title', post_skillset.skill as 'skillset', post.content as 'content', user_view_log.log as 'view_log'" \
                "from user, post, post_skillset, user_view_log where user.email=" \
                + "'" + str(email) + "' " + "and user.email=user_view_log.user_email and user_view_log.post_id=post.id and post.id=post_skillset.post_id"

    cursor.execute(sql_query)
    user_view_log = pd.DataFrame(cursor.fetchall())

    return user_view_log

# email = "a@gmail.com"
# US = _user_skill(email)
# USL= _user_search_log(email)
# UVL = _user_view_log(email)

# print(US)
# print(USL)
# print(UVL.skillset)
# print(UVL.view_log)