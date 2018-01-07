import re


VALID_NAMES_REGEX = '[A-ZА-Я][a-zа-я]+'


def get_initials(name):
    return '.'.join([x.strip()[0] for x in re.findall(VALID_NAMES_REGEX, name)]) + '.'


def main():
    name = input("Enter person's name: ")

    if name:
        print('Initials of "{}" are: {}'.format(name, get_initials(name)))
    else:
        print('Invalid name.')


if __name__ == '__main__':
    main()
