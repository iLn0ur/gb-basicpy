from sys import argv


def add_sale(sum_sale):

    with open('bakery.csv', 'a', encoding='utf-8') as b:
        b.seek(0, 2)
        b.write(sum_sale + '\n')


if __name__ == '__main__':
    add_sale(argv[1])
