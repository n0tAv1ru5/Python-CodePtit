import textwrap

input_str = input()

if len(input_str) % 2 != 0: input_str = input_str[0:-1]

sub_strings = list(textwrap.wrap(input_str, 2))

check = []

for item in sub_strings:
    if item not in check:
        print(item, sub_strings.count(item))
        check.append(item)
