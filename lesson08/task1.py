import re


RE_EMAIL = re.compile(r'(?P<username>\w+)[@](?P<domain>\w+[\.][A-Za-z]{2,4})')


def email_parse(email_address):
    test_str = RE_EMAIL.match(email_address)
    if test_str is None:
        raise ValueError(f'wrong email: {email_address}')
    else:
        result = RE_EMAIL.finditer(email_address)
        for i in result:
            return i.groupdict()


print(email_parse('info@geekbarains.news'))
