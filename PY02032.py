import textwrap

input_str = input()

if len(input_str) % 2 != 0: input_str = input_str[0:-1]

sub_strings = list(textwrap.wrap(input_str, 2))

print(*sorted(set(sub_strings)))
