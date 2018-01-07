STOP_COMMAND = 'stop'
MIN_PRICES = 4


def get_price_statistics(prices):
    prices_count = len(prices)

    if prices_count < MIN_PRICES:
        raise ValueError('Must have at least {} prices!'.format(MIN_PRICES))

    prices.sort()

    min_elements_count = prices.count(prices[0])
    max_elements_count = prices.count(prices[-1])

    elements_without_min_and_max = prices_count - \
        min_elements_count - max_elements_count

    average_without_min_and_max = None
    if min_elements_count == prices_count:
        average_without_min_and_max = 1
    elif elements_without_min_and_max > 0:
        average_without_min_and_max = sum(
            prices[min_elements_count:prices_count - max_elements_count]) / elements_without_min_and_max

    return {
        'min': prices[0] if min_elements_count != prices_count else None,
        'max': prices[-1] if max_elements_count != prices_count else None,
        'average without min and max': average_without_min_and_max
    }


def main():
    prices = _read_prices()

    try:
        print(get_price_statistics(prices))
    except ValueError as e:
        print(e)


def _read_prices():
    prices = []

    while True:
        raw_current_price = input('Enter price: ')
        if raw_current_price == STOP_COMMAND:
            break

        try:
            prices.append(float(raw_current_price))
        except ValueError:
            print('Invalid price!')

    return prices


if __name__ == '__main__':
    main()
