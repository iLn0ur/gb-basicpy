import os


def create_folders(folder_name):
    if folder_name[-1] == '-':
        if not os.path.exists(folder_name[:-1]):
            os.mkdir(folder_name[:-1])
        return True
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    return False


dir_names = list()
with open('folders_name.txt', 'r', encoding='utf-8') as fn:
    for line in fn:
        dir_names.append(line.strip())

master_subf = list()
subf_check_str = '-'
nested_count = 0
for count, el in enumerate(dir_names):
    if el[0:nested_count] == str(subf_check_str * nested_count):
        if create_folders(el[nested_count:]):
            master_subf.append(el[nested_count:-1])
            os.chdir(el[nested_count:-1])
            nested_count += 1
            continue
        # else:

    if el[0] == subf_check_str:
        os.chdir('../')
        nested_count -= 1
        # create_folders()

    # create_folders(el)

print(os.listdir())
