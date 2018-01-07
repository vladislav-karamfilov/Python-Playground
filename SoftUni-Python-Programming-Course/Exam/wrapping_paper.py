import math

PAPER_LOSS_PER_CARTON_PERCENTAGE = 9.8


def _calculate_carton_area(carton_h, carton_w, carton_d):
    return 2 * (carton_h * carton_w + carton_w * carton_d + carton_h * carton_d)


def _get_needed_paper_for_carton_wrapping(carton_area, paper_area):
    needed_paper_without_loss = carton_area / paper_area

    paper_loss = (PAPER_LOSS_PER_CARTON_PERCENTAGE / 100) * \
        needed_paper_without_loss

    needed_paper_with_loss = needed_paper_without_loss + paper_loss

    return math.ceil(needed_paper_with_loss)


def main():
    try:
        paper_area = float(input())
        carton_h = float(input())
        carton_w = float(input())
        carton_d = float(input())

        carton_area = _calculate_carton_area(carton_h, carton_w, carton_d)
        print(_get_needed_paper_for_carton_wrapping(carton_area, paper_area))
    except:
        print('INVALID INPUT')


if __name__ == '__main__':
    main()
