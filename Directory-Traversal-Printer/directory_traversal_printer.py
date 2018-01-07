import os
import sys


def print_directory_traversal(root_dir):
    if not os.path.isdir(root_dir):
        raise ValueError('Directory \'{}\' doesn\'t exist.'.format(root_dir))

    for dir_name, _, file_list in os.walk(root_dir):
        print('Found directory: {}'.format(dir_name))
        for file_name in file_list:
            print('\t{}'.format(file_name))


def main():
    if not sys.argv or len(sys.argv) < 2:
        print('Please specify directory to traverse.')
        return

    root_dir = sys.argv[1]

    try:
        print_directory_traversal(root_dir)
    except ValueError:
        _, ex, _ = sys.exc_info()
        print(ex.args[0])


if __name__ == '__main__':
    main()
