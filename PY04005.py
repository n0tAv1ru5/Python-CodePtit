from decimal import Decimal
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

test_case = list()
for _ in range(int(input())):
    test_case.append(list(map(int, input().split())))
for test in test_case:
    p1 = Point(Decimal(test[0]), Decimal(test[1]))
    p2 = Point(Decimal(test[2]), Decimal(test[3]))
    p3 = Point(Decimal(test[4]), Decimal(test[5]))
    edge1 = p1.distance(p2)
    edge2 = p2.distance(p3)
    edge3 = p3.distance(p1)

    epsilon = 1e-9  # Ngưỡng chính xác
    if abs(edge1 + edge2 - edge3) < epsilon or abs(edge1 + edge3 - edge2) < epsilon or abs(edge2 + edge3 - edge1) < epsilon:
        print("INVALID")
    else:
        print(f"{(edge1 + edge2 + edge3):.3f}")
