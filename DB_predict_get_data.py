import pandas as pd
import pymysql
from DB_connect_setting import DB

cursor = DB.cursor(pymysql.cursors.DictCursor)

def  _user_skill(email):
    sql_query = "select user_skillset.skill as 'user_skill' from user, user_skillset where user.email=" + "'" + str(email) + "'" + "and user.email=user_skillset.user_email order by user_skillset.skill DESC LIMIT 20"

    cursor.execute(sql_query)
    user_skill = pd.DataFrame(cursor.fetchall())

    return user_skill

def _user_search_log(email):
    sql_query = "select user_search_log.log as 'search_log' from user, user_search_log where user.email=" + "'" + str(email) + "'" + "and user.email=user_search_log.user_email order by user_search_log.log DESC LIMIT 20"

    cursor.execute(sql_query)
    user_search_log = pd.DataFrame(cursor.fetchall())

    return user_search_log

def _post_list(email):
    sql_query = "select post.id as 'id', post.title as 'title', post_skillset.skill as 'skillset', post.content as 'content', user_view_log.log as 'view_log' from user, post, user_view_log, post_skillset, member where user.email=member.user_email and member.project_id!=post.id"


# PyMySQL Tester
# def test(email):
#     US = _user_skill(email)
#     USL= _user_search_log(email)
#     UVL = _user_view_log(email)
#     OVL = _other_view_log(email)
#
#     print("[US]\n", US, "\n")
#     print("[USL]\n", USL, "\n")
#     print("[UVL]\n", UVL, "\n")
#     print("[OVL]\n", OVL, "\n")