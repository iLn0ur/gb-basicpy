import os

dir_name = 'my_project'
subfolders_name =['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    os.chdir(dir_name)

for el in subfolders_name:
    if not os.path.exists(el):
        os.mkdir(el)
