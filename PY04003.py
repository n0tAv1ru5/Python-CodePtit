from fractions import Fraction

class fraction_template:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def shorten_fractions(self):
        result = Fraction(self.numerator, self.denominator)
        return f"{result.numerator}/{result.denominator}"

numerator, denominator = map(int, input().split())
test_case = fraction_template(numerator, denominator)
print(test_case.shorten_fractions())
