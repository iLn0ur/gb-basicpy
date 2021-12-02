from sys import argv


def show_sales(start_pos=0, end_pos=0):

    with open('bakery.csv', 'r', encoding='utf-8') as b:
        if start_pos == 0 and end_pos == 0:
            bakery_sum = b.readline().strip()
            print(bakery_sum)
            while bakery_sum:
                bakery_sum = b.readline().strip()
                print(bakery_sum)

        elif start_pos > 0:
            bakery_sum = b.readline().strip()
            i = 1
            if i <= start_pos:
                print(bakery_sum)
            while bakery_sum:
                bakery_sum = b.readline().strip()
                i += 1
                if i >= start_pos:
                    if end_pos != 0:
                        if i < end_pos + 1:
                            print(bakery_sum)


if __name__ == '__main__':
    if len(argv) < 2:
        show_sales()

    if len(argv) == 2:
        print(argv[1])
        show_sales(int(argv[1]))

    if len(argv) > 2:
        show_sales(int(argv[1]), int(argv[2]))
