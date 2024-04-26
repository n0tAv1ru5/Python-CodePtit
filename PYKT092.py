class student:
    def __init__(self, number, name, mark, race, region):
        self.number = number
        self.name = name
        
        if region == 1:
            mark += 1.5
        elif region == 2:
            mark += 1
        if race != "Kinh":
            mark += 1.5
        if mark >= 20.5:
            self.status = "Do"
        else:
            self.status = "Truot"
        self.mark = mark
        
    def __lt__(self, other):
        if self.mark == other.mark:
            return self.number < other.number
        return self.mark > other.mark


student_list = list()
for i in range(1, int(input()) + 1):
    number = "TS" + str(i).zfill(2)
    name = (" ".join(list(input().split()))).title()
    mark = float(input())
    race = input()
    region = int(input())
    student_list.append(student(number, name, mark, race, region))
    
student_list = sorted(student_list)
for item in student_list:
    print(item.number, item.name, item.mark, item.status)
