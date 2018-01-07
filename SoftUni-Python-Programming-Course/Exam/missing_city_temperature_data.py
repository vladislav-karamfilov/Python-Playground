import csv
from datetime import datetime


class CityTemperatureEntry:
    def __init__(self, date, city, average_temperature):
        self.date = date
        self.city = city
        self.average_temperature = average_temperature


def _read_city_temperature_data(city_temperature_data_file_path):
    result = []

    with open(city_temperature_data_file_path, encoding='utf-8') as f:
        city_temperature_entry_reader = csv.reader(f)
        for row in city_temperature_entry_reader:
            if any(row):
                if len(row) != 3:
                    raise ValueError('Invalid data in file: {}'.format(row))

                result.append(
                    CityTemperatureEntry(
                        datetime.strptime(row[0], '%Y-%m-%d'),
                        row[1],
                        float(row[2])
                    ))

    return result


def _get_dates_with_cities_without_temperature_data(city_temperature_by_date_data):
    sorted_dates_set = sorted(set([entry.date for entry in city_temperature_by_date_data]))

    cities_by_date = {}

    for date in sorted_dates_set:
        if date not in city_temperature_by_date_data:
            cities_by_date[date] = set()

        for entry in city_temperature_by_date_data:
            if entry.date == date and entry.city not in cities_by_date[date]:
                cities_by_date[date].add(entry.city)

    cities_set = set([entry.city for entry in city_temperature_by_date_data])

    result = []

    for date in sorted_dates_set:
        cities_without_temperature_data = sorted([city for city in cities_set if city not in cities_by_date[date]])

        if cities_without_temperature_data:
            result.append('{},{}'.format(date.date(), ','.join(cities_without_temperature_data)))

    return result


def main():
    try:
        city_temperature_data_file_path = input()

        city_temperature_data = _read_city_temperature_data(city_temperature_data_file_path)

        if not city_temperature_data:
            print('INVALID INPUT')
            return

        dates_with_cities_without_temperature_data = \
            _get_dates_with_cities_without_temperature_data(city_temperature_data)

        if dates_with_cities_without_temperature_data:
            for entry in dates_with_cities_without_temperature_data:
                print(entry)
        else:
            print('ALL DATA AVAILABLE')
    except Exception:
        print('INVALID INPUT')


if __name__ == '__main__':
    main()
