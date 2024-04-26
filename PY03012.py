class student:
    def __init__(self, name, AC, submit):
        self.name = name
        self.AC = AC
        self.submit = submit

    def __lt__(self, other):
        if self.AC == other.AC:
            return self.name < other.name
        return self.AC > other.AC


student_list = list()
for _ in range(int(input())):
    name = input()
    AC, submit = map(int, input().split())
    student_list.append(student(name, AC, submit))
student_list = sorted(student_list)

for item in student_list:
    print(item.name, item.AC, item.submit)
