import turtle


def main():
    turtle.color('green')

    while True:
        length = int(input('Enter line length: '))
        degree = int(input('Enter degree: '))
        turtle.right(degree)
        turtle.forward(length)


if __name__ == '__main__':
    main()
