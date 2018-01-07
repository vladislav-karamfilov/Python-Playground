import sys
from pprint import pprint as pp


def get_average_price_of_products(products_csv_file_path):
    sum_of_prices = 0
    count_of_product = 0

    with open(products_csv_file_path) as products_csv_file:
        for line in products_csv_file:
            last_index_of_comma = line.rfind(',')
            if last_index_of_comma >= 0:
                price = float(line[last_index_of_comma + 1:])
                sum_of_prices += price
                count_of_product += 1

    return sum_of_prices / count_of_product if count_of_product > 0 else None


def get_average_price_of_products_by_category(products_csv_file_path):
    average_prices_of_products_by_category = {}

    with open(products_csv_file_path) as products_csv_file:
        for line in products_csv_file:
            last_index_of_comma = line.rfind(',')
            if last_index_of_comma >= 0:
                price = float(line[last_index_of_comma + 1:])
                category = line[line.rfind(
                    ',', 0, last_index_of_comma) + 1:last_index_of_comma]

                if category not in average_prices_of_products_by_category:
                    average_prices_of_products_by_category[category] = {
                        'sum': 0,
                        'count': 0
                    }

                average_prices_of_products_by_category[category]['sum'] += price
                average_prices_of_products_by_category[category]['count'] += 1

    return {category_name: average_prices_of_products_by_category[category_name]['sum'] /
            average_prices_of_products_by_category[category_name]['count']
            for category_name in average_prices_of_products_by_category}


def main():
    if not sys.argv or len(sys.argv) < 2:
        print('Please specify products.csv file path.')
        return

    products_csv_file_path = sys.argv[1]
    print('The average price of the products in file "{}" are:'.format(
        products_csv_file_path))
    pp(get_average_price_of_products_by_category(products_csv_file_path))


if __name__ == '__main__':
    main()
