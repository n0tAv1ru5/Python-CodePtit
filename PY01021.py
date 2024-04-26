for _ in range(int(input())):
    input_str = input()
    alphabet = []
    numeric = []
    for char in input_str:
        if char.isnumeric():
            numeric.append(int(char))
        else:
            alphabet.append(char)
    print(*sorted(alphabet), sum(numeric), sep="")
