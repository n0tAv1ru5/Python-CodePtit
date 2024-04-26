input_text = []

try:
    while True:
        input_text.extend(input().split())
except EOFError:
    pass

input_text = list(map(lambda x: x.lower(), input_text))

first_flag = True
line_break = {".", "?", "!"}

for item in input_text:
    
    if first_flag:
        if item[0] in line_break:
            item = item[1:]
        print(item.capitalize(), end="")
        first_flag = False
        
    elif set(item) < line_break and first_flag != True:
        print()
        first_flag = True
    elif set(item) < line_break and first_flag == True:
        pass
    elif any(char in line_break for char in item):
        word = "".join(x for x in item if x not in line_break)
        if item[0] in line_break:
            print()
            print (word.capitalize() ,end="")
        else:
            print(f" {word}")
            first_flag = True
    else:
        print(f" {item}", end="")
