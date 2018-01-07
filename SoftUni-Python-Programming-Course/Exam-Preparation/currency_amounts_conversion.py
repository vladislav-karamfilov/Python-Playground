# Problem description: http://python3.softuni.bg/student/lecture/assignment/56b7295a7e4f59b64bb7e629/


class CurrencyAmount:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


def read_exchange_rates(exchange_rates_file_path):
    exchange_rates = {}

    with open(exchange_rates_file_path, encoding='utf-8') as f:
        for line in f:
            if line and not line.isspace():
                exchange_rate_info = line.split()
                exchange_rates[exchange_rate_info[0]] = float(exchange_rate_info[1])

    return exchange_rates


def read_currency_amounts(amounts_file_path):
    result = []

    with open(amounts_file_path, encoding='utf-8') as f:
        for line in f:
            if line and not line.isspace():
                currency_amount_info = line.split()
                result.append(CurrencyAmount(currency_amount_info[1], float(currency_amount_info[0])))

    return result


def get_amounts_in_bg_leva(exchange_rates, currency_amounts):
    result = []

    for currency_amount in currency_amounts:
        result.append(currency_amount.amount / exchange_rates[currency_amount.currency])

    return result


def main():
    exchange_rates = read_exchange_rates(input())
    currency_amounts = read_currency_amounts(input())

    amounts_in_bg_leva = get_amounts_in_bg_leva(exchange_rates, currency_amounts)
    for amount in amounts_in_bg_leva:
        print('{0:.2f}'.format(amount))


if __name__ == '__main__':
    main()
