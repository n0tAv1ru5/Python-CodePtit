input_data = input()
while len(input_data) > 1:
    sep = len(input_data) // 2
    num_1 = input_data[:sep]
    num_2 = input_data[sep:]
    input_data = int(num_1) + int(num_2)
    print(input_data)
    input_data = str(input_data)
