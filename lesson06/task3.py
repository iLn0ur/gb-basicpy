import sys
import json


users_dict = dict()
string_cursor = 0

with open('users.csv', 'r', encoding='utf-8') as u:
    user_line = u.readline().strip()
    while user_line:
        with open('hobby.csv', 'r', encoding='utf-8') as h:
            h.seek(string_cursor)
            hobby_line = h.readline().strip()
            if hobby_line != '':
                users_dict[user_line] = hobby_line
                string_cursor = h.tell()
            else:
                users_dict[user_line] = None
        user_line = u.readline().strip()
        if user_line != '':
            continue
        else:
            with open('hobby.csv', 'r', encoding='utf-8') as h:
                h.seek(string_cursor)
                hobby_line = h.readline().strip()
                if hobby_line != '':
                    sys.exit(1)

with open('users_hobby.csv', 'w', encoding='utf-8') as uh:
    json.dump(users_dict, uh, ensure_ascii=False, indent=4)
