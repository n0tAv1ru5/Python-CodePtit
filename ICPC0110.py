import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    
    first = second = third = float('-inf')
    
    for num in map(int, input().split()):
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num
    
    print(first + second + third)
