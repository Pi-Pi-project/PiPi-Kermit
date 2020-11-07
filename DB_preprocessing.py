import pandas as pd
from DB_connect_setting import DB
from DB_get_data import _user_skill, _user_search_log, _user_view_log, df_information

email = "a@gmail.com"

try:
    # Get Data from MySQL DB
    user_skill_df = _user_skill(email)
    user_search_log_df = _user_search_log(email)
    user_view_log_df = _user_view_log(email)

finally:
    DB.close()

# df_information(user_skill_df)
# df_information(user_search_log_df)
# df_information(user_view_log_df)

user_skill_list = list(user_skill_df["user_skill"])
user_search_log_list = list(user_search_log_df["search_log"].loc[:len(user_search_log_df)-5:-1]).reverse()
user_view_log_title_list = list(user_view_log_df.loc[:len(user_view_log_df)-5-1, ["title"]]).reverse()
user_view_log_content_list = list(user_view_log_df.loc[:len(user_view_log_df)-5-1, ["post_content"]]).reverse()
user_view_log_list = list(user_view_log_df.loc[:len(user_view_log_df)-5:-1, ["view_log"]]).reverse()