import cmath


class complex_numbers:
    def __init__(self, a, b, c, d):
        self.num_1 = complex(a, b)
        self.num_2 = complex(c, d)

    def calculate_1(self):
        cal_1 = (self.num_1 + self.num_2) * self.num_1
        if cal_1.imag > 0:
            return f"{int(cal_1.real)} + {int(cal_1.imag)}i"
        else:
            return f"{int(cal_1.real)} - {int(-cal_1.imag)}i"

    def calculate_2(self):
        cal_2 = (self.num_1 + self.num_2) ** 2
        if cal_2.imag > 0:
            return f"{int(cal_2.real)} + {int(cal_2.imag)}i"
        else:
            return f"{int(cal_2.real)} - {int(-cal_2.imag)}i"


for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    ans = complex_numbers(a, b, c, d)
    print(f"{ans.calculate_1()}, {ans.calculate_2()}")