from urllib import request
import re


RE_REQ = re.compile(r'(.*)\s-\s-\s\[(.*)\]\s"([A-Z]+)\s(.*)\sH.*"\s(\d+)\s(\d+)')
with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
    base = [RE_REQ.findall(str(line)) for line in log_file]
