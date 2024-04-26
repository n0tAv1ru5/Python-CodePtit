class candidates:
    def __init__(self, number, name, code, score_1, score_2):
        self.number = number
        self.name = name

        if code[1] == "1":
            self.total_score = score_1 * 2 + score_2 + 2.0
        elif code[1] == "2":
            self.total_score = score_1 * 2 + score_2 + 1.5
        elif code[1] == "3":
            self.total_score = score_1 * 2 + score_2 + 1.0
        elif code[1] == "4":
            self.total_score = score_1 * 2 + score_2 + 0.0

        if code[0] == "A":
            self.subject = "TOAN"
        elif code[0] == "B":
            self.subject = "LY"
        else:
            self.subject = "HOA"

        if self.total_score >= 18:
            self.status = "TRUNG TUYEN"
        else:
            self.status = "LOAI"

    def __lt__(self, other):
        if self.total_score == other.total_score:
            return self.number < other.number
        return self.total_score > other.total_score


candidates_list = list()
for i in range(int(input())):
    number = "GV" + str(i + 1).zfill(2)
    name = input()
    code = input()
    score_1 = float(input())
    score_2 = float(input())
    candidates_list.append(candidates(number, name, code, score_1, score_2))
candidates_list = sorted(candidates_list)

for item in candidates_list:
    print(item.number, item.name, item.subject, item.total_score, item.status)
