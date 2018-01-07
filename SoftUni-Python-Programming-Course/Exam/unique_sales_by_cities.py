import csv


class SimpleSaleInfo:
    def __init__(self, city, item):
        self.city = city
        self.item = item


def _read_sales(sales_file_path):
    sales = []

    with open(sales_file_path, encoding='utf-8') as f:
        sales_reader = csv.reader(f)
        for row in sales_reader:
            if any(row):
                if len(row) != 5:
                    raise ValueError('Invalid data in file: {}'.format(row))

                sales.append(SimpleSaleInfo(row[2], row[0]))

    return sales


def _get_cities_with_unique_item_sales(sales):
    result = []

    items_set = set([sale.item for sale in sales])

    cities_by_item = {}
    for item in items_set:
        if item not in cities_by_item:
            cities_by_item[item] = set()

        for sale in sales:
            if sale.item == item and sale.city not in cities_by_item[item]:
                cities_by_item[item].add(sale.city)

    sorted_cities_set = sorted(set([sale.city for sale in sales]))

    for city in sorted_cities_set:
        unique_sale_items_in_city = sorted(
            [item for _, item in enumerate(cities_by_item)
                if len(cities_by_item[item]) == 1 and city in cities_by_item[item]])

        if unique_sale_items_in_city:
            result.append('{},{}'.format(city, ','.join(unique_sale_items_in_city)))

    return result


def main():
    try:
        sales_file_path = input()
        sales = _read_sales(sales_file_path)

        if not sales:
            print('INVALID INPUT')
            return

        cities_with_unique_item_sales = _get_cities_with_unique_item_sales(sales)

        if cities_with_unique_item_sales:
            for entry in cities_with_unique_item_sales:
                print(entry)
        else:
            print('NO UNIQUE SALES')
    except Exception as e:
        print('INVALID INPUT')


if __name__ == '__main__':
    main()
