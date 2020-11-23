from Preprocessing_Func import get_data, lower, regex, nouns

# Test Email
email = "a@gmail.com"

"""
US: User_Skillset - user_skill
USL: User_Search_Log - search_log
UVL: User_View_Log - id, title, skillset, content, view_log
"""
US, USL, UVL = get_data(email)

US.user_skill = lower(US.user_skill)
USL.search_log = lower(USL.search_log)
UVL.title = nouns(regex(lower(UVL.title)))
UVL.skillset = lower(UVL.skillset)
UVL.content = nouns(regex(lower(UVL.content)))
UVL.view_log = lower(UVL.view_log)