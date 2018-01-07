import sys


def read_interests(input_stream, output_stream=None):
    if output_stream is None:
        output_stream = sys.stdout

    interests = []
    while True:
        output_stream.write('Enter an interest (empty string to end): ')
        output_stream.flush()

        interest = input_stream.readline()

        if interest == '\n':
            break

        interests.append(interest[:len(interest) - 1])

    return interests


if __name__ == '__main__':
    print('***Get the common interests of two people***')

    first_person_name = input('Enter first person name: ')
    second_person_name = input('Enter second person name: ')
    print()

    print("---{}'s interests---".format(first_person_name))
    first_person_interests = read_interests(sys.stdin)
    print()

    print("---{}'s interests---".format(second_person_name))
    second_person_interests = read_interests(sys.stdin)
    print()

    common_interests = set(first_person_interests).intersection(
        set(second_person_interests))
    print('Common interests of {} and {}: {}'.format(
        first_person_name, second_person_name, common_interests or ''))
