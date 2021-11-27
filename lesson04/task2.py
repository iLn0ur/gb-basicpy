import requests


def currency_rates(curr_to_find: str) -> float:
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    curr_value_dict = {}
    curr_name = ''
    for curr_box in content.split('<Valute ID="'[1:]):
        for box in curr_box.split('><'):

            if box.find('CharCode>') != -1:
                curr_name = box[9:12]
            if box.find('Value>') != -1:
                curr_value = float(box[6:13].replace(',', '.'))
                curr_value_dict.update({curr_name: curr_value})
    return curr_value_dict.get(curr_to_find)


if __name__ == '__main__':
    print(currency_rates("AUD"))
