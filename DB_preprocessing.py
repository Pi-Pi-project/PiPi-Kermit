import pandas as pd
from DB_connect_setting import DB
from DB_get_data import _user_skill, _user_search_log, _user_view_log, df_information

email = "a@gmail.com"

try:
    user_skill = _user_skill(email)
    user_search_log = _user_search_log(email)
    user_view_log = _user_view_log(email)

finally:
    DB.close()

df_information(user_skill)
df_information(user_search_log)
df_information(user_view_log)