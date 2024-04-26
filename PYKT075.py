class dial:
    def __init__(self, date, name, phone_number):
        self.date = (date.split())[1]
        self.name = name
        self.phone_number = phone_number

    def __lt__(self, other):
        if ((self.name).split())[-1] == ((other.name).split())[-1]:
            return ((self.name).split())[-2] < ((other.name).split())[-2]
        return ((self.name).split())[-1] < ((other.name).split())[-1]


with open("SOTAY.txt", "r") as file:
    lines = []
    for line in file: 
        lines.append(line.rstrip('\n'))
        
for 