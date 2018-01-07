# Problem description: http://python3.softuni.bg/student/lecture/assignment/56b716187e4f59b64ab7e5ef/

from math import sqrt


def calculate_triangle_area(a, b, c):
    half_perimeter = (a + b + c) / 2
    return sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c))


def main():
    try:
        a = float(input())
        b = float(input())
        c = float(input())
        print("{0:.2f}".format(calculate_triangle_area(a, b, c)))
    except:
        print('INVALID INPUT')


if __name__ == '__main__':
    main()
