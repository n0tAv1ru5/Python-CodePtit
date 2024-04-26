from decimal import Decimal
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

t = int(input())
while t > 0:
    arr = input().split()
    p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
    p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
    print(f"{p1.distance(p2):.4f}")
    t -= 1

