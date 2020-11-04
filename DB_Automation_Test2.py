import pymysql
import pandas as pd
import numpy as np
from db_connect_setting import DB

email = "a@gmail.com"

def _user_skill(email):
    sql_query = "select user.email as 'email', user_skillset.skill as 'user_skill' from user, user_skillset where user.email=" \
                + "'" + str(email) + "' " + "and user.email=user_skillset.user_email;"

    skill_cursor = DB.cursor(pymysql.cursors.DictCursor)
    skill_cursor.execute(sql_query)
    skill_result = skill_cursor.fetchall()

    DB.close()

    return pd.DataFrame(skill_result)

def _user_search_log(email):
    sql_query = "select user.email as 'email', user_search_log.log as 'search_log' from user, user_search_log" \
                + "'" + str(email) + "' " + "and user.email=user_search_log.user_email;"

    search_cursor = DB.cursor(pymysql.cursors.DictCursor)
    search_cursor.execute(sql_query)
    search_result = search_cursor.fetchall()

    DB.close()

    return pd.DataFrame(search_result)

def _user_view_log(email):
    sql_query = "select user.email as 'email', post.id as 'post_id', post.title as 'title', post.content as 'post_content', user_view_log.log as 'view_log'" \
                + "'" + str(email) + "' " + "and user.email=user_view_log.user_email;"

    view_cursor = DB.cursor(pymysql.cursors.DictCursor)
    view_cursor.execute(sql_query)
    view_result = view_cursor.fetchall()

    DB.close()

    return pd.DataFrame(view_result)

print("[Skill result]")
print(_user_skill(email))

print("[Search log result]")
print(_user_search_log(email))

print("[View log result]")
print(_user_view_log(email))

