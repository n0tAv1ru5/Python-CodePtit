import math


class tier_list:
    def __init__(self, code, name, average):
        self.code = code
        self.name = name
        self.average = average

    def __lt__(self, other):
        if self.average == other.average:
            return self.code < other.code
        else:
            return self.average > other.average

    def ranking(self):
        if self.average >= 9:
            self.rank = "XUAT SAC"
        elif 8 <= self.average < 9:
            self.rank = "GIOI"
        elif 7 <= self.average < 8:
            self.rank = "KHA"
        elif 5 <= self.average < 7:
            self.rank = "TB"
        else:
            self.rank = "YEU"
        return self.rank


student_list = list()

for i in range(int(input())):
    code = f"HS{str(i+1).zfill(2)}"
    name = input()
    score = list(map(float, input().split()))
    average = round((2 * sum(score[:2]) + sum(score[2:])) / 10 /1.2, 1)

   
    student = tier_list(code, name, average)
    student_list.append(student)
student_list.sort()

for student in student_list:
    print(f"{student.code} {student.name} {student.average} {student.ranking()}")