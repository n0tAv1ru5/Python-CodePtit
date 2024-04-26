fee_list = {"5": 10000, "7": 15000, "2": 20000, "29": 50000, "45": 70000}

car_list = dict()
for _ in range(int(input())):
    input_data = input()
    if "OUT" in input_data:
        continue
    input_data = input_data.split()
    if input_data[-1] not in car_list:
        car_list[input_data[-1]] = fee_list[input_data[-3]]
    else:
        car_list[input_data[-1]] += fee_list[input_data[-3]]

for key, val in car_list.items():
    print(f"{key}: {val}")
