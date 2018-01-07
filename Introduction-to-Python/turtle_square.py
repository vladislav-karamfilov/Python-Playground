import turtle

SQUARE_SIDES = 4


def main():
    side_length = int(input('Enter square side length: '))
    line_color = input('Enter square line color: ')
    drawing_speed = input(
        'Enter drawing speed - "fastest", "fast", "normal", "slow" or "slowest": ')
    drawing_direction = input(
        'Enter drawing direction - "forward" or "backward": ')
    drawing_turn_direction = input(
        'Enter drawing turn direction - "left" or "right": ')

    turtle.color(line_color)
    turtle.speed(drawing_speed)

    for _ in range(SQUARE_SIDES):
        if drawing_direction == 'forward':
            turtle.forward(side_length)
        elif drawing_direction == 'backward':
            turtle.backward(side_length)
        else:
            raise ValueError('Invalid drawing direction.')

        if drawing_turn_direction == 'left':
            turtle.left(90)
        elif drawing_turn_direction == 'right':
            turtle.right(90)
        else:
            raise ValueError('Invalid drawing turn direction.')


if __name__ == '__main__':
    main()
