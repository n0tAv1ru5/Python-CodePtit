from collections import Counter


text_list = list()
n = int( input())

for _ in range(n):
    input_text = input()
    for char in input_text:
        if not char.isalnum() or char.isnumeric(): 
            input_text = input_text.replace(char, " ")
    text_list.extend(map(lambda x: x.lower(), input_text.split()))
    
text_counter = Counter(text_list)
unpacked_text_counter = []

for key, val in text_counter.items():
    unpacked_text_counter.append((key, val))
for key, val in sorted(unpacked_text_counter, key=lambda x: (-x[1], x[0])):   
        print(key,val)
    
