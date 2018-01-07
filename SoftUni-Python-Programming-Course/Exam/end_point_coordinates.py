LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction, delta):
        if direction == RIGHT:
            self.x += delta
        elif direction == LEFT:
            self.x -= delta
        elif direction == UP:
            self.y += delta
        elif direction == DOWN:
            self.y -= delta
        else:
            raise ValueError('Invalid direction!')


def _calculate_end_point(steps_file_path):
    point = None

    with open(steps_file_path, encoding='utf-8') as f:
        for line in f:
            if line and not line.isspace():
                step_info = line.split()

                direction = step_info[0]
                delta = float(step_info[1])

                if point is None:
                    point = Point(0, 0)

                point.move(direction, delta)

    return point


def main():
    try:
        steps_file_path = input()
        end_point = _calculate_end_point(steps_file_path)
        print('X {0:.3f}'.format(end_point.x))
        print('Y {0:.3f}'.format(end_point.y))
    except:
        print('INVALID INPUT')


if __name__ == '__main__':
    main()
