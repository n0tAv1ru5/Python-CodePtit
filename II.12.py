from datetime import datetime

start_time = input()
end_time = input()

start_datetime = datetime.strptime(start_time, "%H %M %S")
end_datetime = datetime.strptime(end_time, "%H %M %S")

running_time_seconds = (end_datetime - start_datetime).total_seconds()

if running_time_seconds < 0:
    running_time_seconds += 24 * 3600  

print(int(running_time_seconds))
