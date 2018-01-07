# Problem description: http://python3.softuni.bg/student/lecture/assignment/56b9e72c7e4f59b649b7e64b/

import re


def get_city_with_least_item_price(item, sales_file_path):
    result = None
    min_price = float('+inf')

    with open(sales_file_path, encoding='utf-8') as f:
        for line in f:
            if line:
                sale_item_info = line.split(',')
                current_item = re.sub('[ "]', '', sale_item_info[0])
                if current_item == item:
                    price = float(sale_item_info[-1])
                    if price < min_price:
                        min_price = price
                        result = re.sub('[ "]', '', sale_item_info[2])

    return result


def main():
    item = input()

    sales_file_path = input()

    print(get_city_with_least_item_price(item, sales_file_path))


if __name__ == '__main__':
    main()
