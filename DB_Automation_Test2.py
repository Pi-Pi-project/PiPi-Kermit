import pymysql
import pandas as pd
import numpy as np
from db_connect_setting import DB

email = "a@gmail.com"

def  _user_skill(email):
    sql_query = "select user.email as 'email', user_skillset.skill as 'user_skill' from user, user_skillset where user.email=" \
                + "'" + str(email) + "' " + "and user.email=user_skillset.user_email;"

    return sql_query

def _user_search_log(email):
    sql_query = "select user.email as 'email', user_search_log.log as 'search_log' from user, user_search_log" \
                + "'" + str(email) + "' " + "and user.email=user_search_log.user_email;"

    return sql_query

def _user_view_log(email):
    sql_query = "select user.email as 'email', post.id as 'post_id', post.title as 'title', post.content as 'post_content', user_view_log.log as 'view_log'" \
                + "'" + str(email) + "' " + "and user.email=user_view_log.user_email;"

    return sql_query

cursor = DB.cursor(pymysql.cursors.DictCursor)

cursor.execute(_user_skill(email))
skill_result = cursor.fetchall()

cursor.execute(_user_search_log(email))
search_result = cursor.fetchall()

cursor.execute(_user_view_log(email))
view_result = cursor.fetchall()

DB.close()