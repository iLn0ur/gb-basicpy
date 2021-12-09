spam_find = dict()
max_requests = 0

with open('nginx_logs.txt', 'r', encoding='utf-8') as ng:
    line = (ng.readline().strip().split())
    while line:
        if line[0] in spam_find:
            spam_find[line[0]] += 1
        else:
            spam_find[line[0]] = 0
        if max_requests < spam_find[line[0]]:
            max_requests = spam_find[line[0]]
            ip_spammer = line[0]
        line = ng.readline().strip().split()


print(ip_spammer, spam_find[ip_spammer])
