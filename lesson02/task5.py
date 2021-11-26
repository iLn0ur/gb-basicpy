import random


def format_output(price_list_sample: list):
    for count, el in enumerate(price_list_sample):
        temp_price = str(int((el * 100) // 100)).rjust(2, '0') + ' руб ' + \
                     str(int((el * 100) % 100)).rjust(2, '0') + ' коп'
        price_list_sample[count] = temp_price
        print(price_list_sample[count])


price_list = [round(random.uniform(0, 100), 2) for _ in range(20)]
print(price_list)
price_list.sort()
price_list_reverse = price_list.copy()
format_output(price_list)
price_list_reverse.reverse()
print(price_list_reverse)
format_output(price_list_reverse)


