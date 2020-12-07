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
    sql_query = "select post.id as 'id', post.title as 'title', post.img as 'img', post.category as 'cate', post.idea as 'idea', post_skillset.skill as 'skillset', post.max as 'max', post.user_email as 'email', user.profile_image as 'profile_img', user.nickname as 'nickname', post.created_at as 'created', post.content as 'content', user_view_log.log as 'view_log' from user, post, user_view_log, post_skillset, member where user.email=" + "'" + str(email) + "'" + "and user.email=member.user_email and member.project_id!=post.id order by user.nickname DESC LIMIT 40"

    cursor.execute(sql_query)
    post_list = pd.DataFrame(cursor.fetchall())

    return post_list

# PyMySQL Tester
# def test(email):
#     US = _user_skill(email)
#     USL= _user_search_log(email)
#     PL = _post_list(email)
#
#     print("[US]\n", US, "\n")
#     print("[USL]\n", USL, "\n")
#     print("[PL]\n", PL, "\n")
#
# test("a@gmail.com")