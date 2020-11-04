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
select user.email as 'email', post.id as 'post_id', post.title as 'title', post.content as 'post_content', user_view_log.log as 'view_log'
from user, user_view_log, post
where user.email='a@gmail.com' and user.email=user_view_log.user_email and user_view_log.id=post.id;
"""

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

skill_cursor = DB.cursor(pymysql.cursors.DictCursor)
search_cursor = DB.cursor(pymysql.cursors.DictCursor)
view_cursor = DB.cursor(pymysql.cursors.DictCursor)

skill_cursor.execute(_user_skill("a@gmail.com"))
search_cursor.execute(_user_search_log("a@gmail.com"))
view_cursor.execute(_user_view_log("a@gmail.com"))

skill_result = skill_cursor.fetchall()
search_result = search_cursor.fetchall()
view_result = view_cursor.fetchall()

skill_pd_result = pd.DataFrame(skill_result)
search_pd_result = pd.DataFrame(search_result)
view_pd_result = pd.DataFrame(view_result)

print("Skill result")
print(skill_pd_result)

print("Search log result")
print(search_pd_result)

print("View log result")
print(view_pd_result)

DB.close()