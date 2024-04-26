m = int(input())  
v = int(input())  
t = int(input()) 
d = input()       

distance = v * t

if d == 'C':
    final_position = distance % m
else:
    final_position = (m - (distance % m)) % m

print(final_position)
