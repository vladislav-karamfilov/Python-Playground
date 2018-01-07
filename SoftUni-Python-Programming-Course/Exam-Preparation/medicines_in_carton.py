# Problem description: http://python3.softuni.bg/student/lecture/assignment/56b749af7e4f59b649b7e626/


class Medicine:
    def __init__(self, name, w, h, d):
        self.name = name
        self.w = w
        self.h = h
        self.d = d

    def can_be_put_in_carton(self, carton_w, carton_h, carton_d):
        sorted_medicine_dimensions = sorted([self.w, self.h, self.d])
        sorted_carton_dimensions = sorted([carton_w, carton_h, carton_d])

        return all(sorted_medicine_dimensions[d] <= sorted_carton_dimensions[d] for d in range(3))


def read_medicines(medicines_file_path):
    result = []

    with open(medicines_file_path, encoding='utf-8') as f:
        for line in f:
            if line:
                medicine_info = line.split(',')

                medicine_name = ''.join(medicine_info[:-3])
                medicine_w = float(medicine_info[-3])
                medicine_h = float(medicine_info[-2])
                medicine_d = float(medicine_info[-1])

                result.append(Medicine(medicine_name, medicine_w, medicine_h, medicine_d))

    return result


def main():
    try:
        carton_w = float(input())
        carton_h = float(input())
        carton_d = float(input())

        medicines_file_path = input()
        medicines = read_medicines(medicines_file_path)
    except:
        print('INVALID INPUT')
        return

    medicines_that_can_be_put_in_carton = \
        [medicine for medicine in medicines if medicine.can_be_put_in_carton(carton_w, carton_h, carton_d)]

    for medicine in medicines_that_can_be_put_in_carton:
        print(medicine.name)

if __name__ == '__main__':
    main()
