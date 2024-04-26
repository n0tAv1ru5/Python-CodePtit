from fractions import Fraction

class fraction_template:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def adding(self, other_fraction):
        result = Fraction(self.numerator, self.denominator) + Fraction(other_fraction.numerator, other_fraction.denominator)
        return f"{result.numerator}/{result.denominator}"

nums_arr = list(map(int, input().split()))
frac_1 = fraction_template(nums_arr[0], nums_arr[1])
frac_2 = fraction_template(nums_arr[2], nums_arr[3])
print(frac_1.adding(frac_2))
