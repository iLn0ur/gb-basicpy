import requests
import datetime


def currency_rates(curr_to_find: str):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    curr_name = ''
    start = content.find(" Date=")
    print(content[start + 7: start + 17])
    curr_value_dict = {}
    curr_value_dict.update({"Date": datetime.datetime.
                           strptime(str(content[start + 7: start + 17]), "%d.%m.%Y").strftime("%d/%m/%Y")})
    for curr_box in content.split('<Valute ID="'[1:]):
        for box in curr_box.split('><'):

            if box.find('CharCode>') != -1:
                curr_name = box[9:12]
            if box.find('Value>') != -1:
                curr_value = float(box[6:13].replace(',', '.'))
                curr_value_dict.update({curr_name: curr_value})
        # print(curr_box)
    return curr_value_dict.get("Date"), curr_value_dict.get(curr_to_find)


if __name__ == '__main__':
    print(currency_rates("AUD"))
