from collections import Counter

text_list = list()
for _ in range(int(input())):
    input_text = input()
    for char in input_text:
        if not char.isalnum(): 
            input_text = input_text.replace(char, " ")
    text_list.extend(map(lambda x: x.lower(), input_text.split()))

text_counter = Counter(text_list)
unpacked_text_counter = []
for key, val in text_counter.items():
    unpacked_text_counter.append((key, val))
for item in sorted(unpacked_text_counter, key=lambda x: (-x[1], x[0])):
    print(*item)
