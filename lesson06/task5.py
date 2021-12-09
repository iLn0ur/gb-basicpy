import sys
import json
import pathlib
from pathlib import Path


def transform_user_hobby(users_path=str(Path(pathlib.Path.cwd(), 'users.csv')),
                         hobby_path=str(Path(pathlib.Path.cwd(), 'hobby.csv')),
                         exit_path=str(Path(pathlib.Path.cwd(), 'users_hobby.csv'))):
    users_dict = dict()
    string_cursor = 0
    with open(users_path, 'r', encoding='utf-8') as u:
        user_line = u.readline().strip()
        while user_line:
            with open(hobby_path, 'r', encoding='utf-8') as h:
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

    with open(exit_path, 'w', encoding='utf-8') as uh:
        json.dump(users_dict, uh, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    ques1 = input('Please enter "2" to input path: ')
    if ques1 == '2':
        path1 = input('Please enter path to users file: ')
        path2 = input('Please enter path to hobby file: ')
        path3 = input('Please enter path to users_hobby file: ')
        transform_user_hobby(path1, path2, path3)
    else:
        transform_user_hobby()
