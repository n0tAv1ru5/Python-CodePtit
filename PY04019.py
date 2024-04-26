import math


class employee:
    def __init__(self, number, name, point, status):
        self.number = number
        self.name = name
        self.point = point
        self.status = status

    def __lt__(self, other):
        return float(self.point) > float(other.point)


employee_list = list()

for i in range(1, int(input()) + 1):

    number = "TS0" + f"{i}"
    name = input()
    point_1 = float(input())
    point_2 = float(input())

    if point_1 > 10:
        point_1 /= 10
    if point_2 > 10:
        point_2 /= 10
    point = f"{((point_1 + point_2) / 2.0):.2f}"

    if float(point) < 5:
        status = "TRUOT"
    elif 5 <= float(point) < 8:
        status = "CAN NHAC"
    elif 8 <= float(point) <= 9.5:
        status = "DAT"
    else:
        status = "XUAT SAC"

    person = employee(number, name, point, status)
    employee_list.append(person)
    

employee_list = sorted(employee_list)

for item in employee_list:
    print(item.number, item.name, item.point, item.status)
