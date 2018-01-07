# Problem description: http://python3.softuni.bg/student/lecture/assignment/56ba27d67e4f59b64bb7e66b/


def get_trip_time(file_path):
    trip_time = 0

    with open(file_path, encoding='utf-8') as f:
        for line in f:
            if line:
                distance_info = line.split(',')

                distance_from = int(distance_info[0])
                distance_to = int(distance_info[1])
                distance_speed_limit = int(distance_info[2])

                trip_time += (distance_to - distance_from + 1) / distance_speed_limit

    return trip_time


def main():
    try:
        print('{0:.2f}'.format(get_trip_time(input())))
    except:
        print('INVALID INPUT')


if __name__ == '__main__':
    main()
