some_list = list()

with open('nginx_logs.txt', 'r', encoding='utf-8') as ng:
    line = (ng.readline().strip().split())
    while line:
        some_list.append(tuple((line[0], line[5], line[6])))
        line = ng.readline().strip().split()

for el in some_list:
    print(el)
