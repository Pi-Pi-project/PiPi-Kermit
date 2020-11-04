from test_files.DB_skill_test import _user_skill
from test_files.DB_search_test import _user_search_log

email = 'a@gmail.com'

a = _user_search_log(email)
b = _user_skill(email)

print(a)

print(b)