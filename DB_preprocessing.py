import pandas as pd
from DB_connect_setting import DB
from DB_get_data import _user_skill, _user_search_log, _user_view_log

email = ""

try:
    user_skill = _user_skill(email)
    user_search_log = _user_search_log(email)
    user_view_log = _user_view_log(email)

finally:
    DB.close()
