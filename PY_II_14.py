def calculate_hour_hand_angle(h, m, s):
    hour_angle = (h * 30 + m * 0.5 + s * (1 / 120)) / 360 * 360
    return hour_angle


input_data = input()
if ":" in input_data:
    input_data = input_data.split(":")[1]
h, m, s = map(int, input_data.split())

angle = calculate_hour_hand_angle(h, m, s)

print("Angle:",angle)
