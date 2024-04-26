class racer:
    def __init__(self, name, location, time):
        self.name = name
        self.location = location

        self.code = ""

        for char in location.split():
            self.code += char[0]
        for char in name.split():
            self.code += char[0]

        self.hour = int(time.split(":")[0])
        self.minute = int(time.split(":")[1])

        self.v = 120 / (self.hour - 6 + self.minute / 60)

    def __lt__(self, other):
        if self.hour == other.hour:
            return self.minute < other.minute
        return self.hour < other.hour


racer_list = list()

for _ in range(int(input())):
    name = input()
    location = input()
    time = input()
    racer_list.append(racer(name, location, time))
racer_list = sorted(racer_list)

for item in racer_list:
    print(item.code, item.name,item.location, round(item.v), "Km/h")
