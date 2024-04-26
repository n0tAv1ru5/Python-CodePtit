class Gamer:
    def __init__(self, code, name, time_in, time_out):
        self.code = code
        self.name = name
        self.time_in = time_in
        self.time_out = time_out
        self.total_play_times = 0

    def calculate_play_time(self):
        hours_in, minutes_in = map(int, self.time_in.split(':'))
        hours_out, minutes_out = map(int, self.time_out.split(':'))
        total_minutes_in = hours_in * 60 + minutes_in
        total_minutes_out = hours_out * 60 + minutes_out
        self.total_play_times = total_minutes_out - total_minutes_in

    def __lt__(self, other):
        return self.total_play_times > other.total_play_times

gamers = []

for _ in range(int(input())):
    code = input()
    name = input()
    time_in = input()
    time_out = input()

    gamer = Gamer(code, name, time_in, time_out)
    gamers.append(gamer)
    gamer.calculate_play_time()
    
gamers.sort()

for gamer in gamers:
    play_hours, play_minutes = divmod(gamer.total_play_times, 60)
    print(f"{gamer.code} {gamer.name} {play_hours} gio {play_minutes} phut")