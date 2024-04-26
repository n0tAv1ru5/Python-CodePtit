class test:
    def __init__(self, subject_id, subject_name, test_format):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.test_format = test_format

    def __lt__(self, other):
        return self.subject_id < other.subject_id


test_list = list()

for _ in range(int(input())):
    subject_id = input()
    subject_name = input()
    test_format = input()

    test_list.append(test(subject_id, subject_name, test_format))
test_list = sorted(test_list)
for item in test_list:
    print(item.subject_id, item.subject_name, item.test_format)
