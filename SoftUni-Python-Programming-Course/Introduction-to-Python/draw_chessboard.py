import turtle
from random import randint


CHESSBOARD_COLORS = ['black', 'white']
SQUARE_SIDES = 4
SQUARE_SIDE_LENGTH = 15
SQUARE_ANGLE_DEGREE = 90


def draw_chessboard(rows, cols):
    turtle.speed('fastest')
    turtle.bgcolor('red')

    color_index = randint(0, 1)
    turtle.color(CHESSBOARD_COLORS[color_index])

    for _ in range(rows):
        for _ in range(cols):
            turtle.color(CHESSBOARD_COLORS[color_index])

            _draw_square()

            current_position = turtle.position()
            turtle.goto(current_position[0] -
                        SQUARE_SIDE_LENGTH, current_position[1])

            color_index = _get_next_color(color_index)

        color_index = _get_next_color(color_index)
        if cols % 2 == 1:
            color_index = _get_next_color(color_index)

        current_position = turtle.position()
        turtle.goto(current_position[0] + (cols * SQUARE_SIDE_LENGTH),
                    current_position[1] + SQUARE_SIDE_LENGTH)

    turtle.hideturtle()
    turtle.exitonclick()


def main():
    rows = int(input('Enter chessboard rows: '))
    cols = int(input('Enter chessboard columns: '))

    draw_chessboard(rows, cols)


def _draw_square():
    turtle.begin_fill()

    for _ in range(SQUARE_SIDES):
        turtle.pendown()
        turtle.forward(SQUARE_SIDE_LENGTH)
        turtle.left(SQUARE_ANGLE_DEGREE)
        turtle.penup()

    turtle.end_fill()


def _get_next_color(current_color_index):
    if current_color_index == 0:
        return 1

    return 0


if __name__ == '__main__':
    main()
