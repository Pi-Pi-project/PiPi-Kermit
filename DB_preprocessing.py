import pandas as pd
from DB_connect_setting import DB
from DB_get_data import _user_skill, _user_search_log, _user_view_log, df_information

email = "a@gmail.com"

try:
    user_skill_df = _user_skill(email)
    user_search_log_df = _user_search_log(email)
    user_view_log_df = _user_view_log(email)

finally:
    DB.close()

# df_information(user_skill_df)
# df_information(user_search_log_df)
# df_information(user_view_log_df)

user_skill_list = list(user_skill_df["user_skill"])
user_search_log_list = list(user_search_log_df["search_log"])
user_view_log_loc = user_view_log_df.loc[:, ["post_id", "title", "post_content", "view_log"]]

print(user_view_log_loc)

user_view_log_list = []
print(list(user_view_log_loc.loc[0]))

# Get row length
print(len(user_view_log_loc))