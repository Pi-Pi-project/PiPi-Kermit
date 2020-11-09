import pandas as pd
from DB_connect_setting import DB
from DB_get_data import _user_skill, _user_search_log, _user_view_log
from eunjeon import Mecab

mecab = Mecab()

# Test Email
email = "a@gmail.com"

try:
    # Get Data from MySQL DB
    skill_df = _user_skill(email)
    search_log_df = _user_search_log(email)
    view_log_df = _user_view_log(email)

finally:
    # Close the connection from the MySQL DB
    DB.close()

search_log_len = len(search_log_df)
view_log_len = len(view_log_df)

# Conver DataFrame to list
skill_list = list(skill_df["user_skill"])

search_log_list = list(search_log_df["search_log"].iloc[search_log_len-6::1])
search_log_list.reverse()

view_title_list = list(view_log_df["title"].iloc[view_log_len-6::1])
view_title_list.reverse()

view_content_list = list(view_log_df["post_content"].iloc[view_log_len-6::1])
view_content_list.reverse()

view_log_list = list(view_log_df["view_log"].iloc[view_log_len-6::1])
view_log_list.reverse()

# Test
print(skill_list)
print(search_log_list)
print(view_title_list)
print(view_content_list)
print(view_log_list)

# print(mecab.morphs(view_content_list[0]))
# print(mecab.nouns(view_content_list[0]))