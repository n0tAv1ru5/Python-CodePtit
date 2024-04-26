class student:
    def __init__(self, code, name, score_1, score_2, score_3):
        self.name = (" ".join(name.split())).title()
        self.average_score = round((score_1 + score_2 + score_3) / 3, 3)
        self.code = code

    def __lt__(self, other):
        if self.average_score == other.average_score:
            return self.code < other.code
        return self.average_score > other.average_score


student_list = list()

for i in range(int(input())):
    code = "SV" + str(i + 1).zfill(2)
    name = input()
    score_1 = int(input())
    score_2 = int(input())
    score_3 = int(input())

    student_list.append(student(code, name, score_1, score_2, score_3))
student_list = sorted(student_list)
for idx, item in enumerate(student_list):
    print(item.code, item.name, item.average_score, idx + 1)
