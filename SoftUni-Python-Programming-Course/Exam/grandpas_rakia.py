import csv
import math

CENTIMETERS_IN_ONE_DECIMETER = 10


class Container:
    def __init__(self, name, radius_in_decimeters, height_in_decimeters):
        self.name = name
        self.radius = radius_in_decimeters
        self.height = height_in_decimeters

    def get_volume_in_liters(self):
        return math.pi * self.radius * self.radius * self.height


def _read_containers_from_file(containers_csv_file_path):
    containers = []

    with open(containers_csv_file_path, encoding='utf-8') as f:
        containers_reader = csv.reader(f)
        for row in containers_reader:
            if row:
                name = row[0]
                radius_in_centimeters = float(row[1])
                height_in_centimeters = float(row[2])

                if not name or radius_in_centimeters <= 0 or height_in_centimeters <= 0:
                    raise ValueError('Invalid data in file: {}'.format(row))

                containers.append(Container(
                    name,
                    radius_in_centimeters / CENTIMETERS_IN_ONE_DECIMETER,
                    height_in_centimeters / CENTIMETERS_IN_ONE_DECIMETER))

    return containers


def _get_most_suitable_container_for_rakia(rakia_liters, containers):
    result = None

    min_container_volume = float('+inf')

    for container in containers:
        container_volume = container.get_volume_in_liters()
        if rakia_liters <= container_volume < min_container_volume:
            min_container_volume = container_volume
            result = container

    return result


def main():
    try:
        rakia_liters = float(input())
        if rakia_liters <= 0:
            print('INVALID INPUT')
        else:
            containers_file_path = input()

            containers = _read_containers_from_file(containers_file_path)

            most_suitable_container = _get_most_suitable_container_for_rakia(rakia_liters, containers)

            if most_suitable_container is None:
                print('NO SUITABLE CONTAINER')
            else:
                print(most_suitable_container.name)
    except:
        print('INVALID INPUT')


if __name__ == '__main__':
    main()
