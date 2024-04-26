class customer:
    def __init__(self, id, name, total_usage):
        self.id = id
        self.name = name
        self.cost = 0

        if total_usage <= 50:
            self.cost = total_usage * 102
        if 50 < total_usage <= 100:
            self.cost = round((50 * 100 + (total_usage - 50) * 150) * 1.03)
        if total_usage > 100:
            self.cost = round((50 * 100 + 50 * 150 + (total_usage - 100) * 200) * 1.05)

    def __lt__(self, other):
        return self.cost > other.cost


customer_list = list()

for i in range(int(input())):
    id = "KH" + str(i + 1).zfill(2)
    name = input()
    total_usage = -int(input()) + int(input())
    customer_list.append(customer(id, name, total_usage))
customer_list = sorted(customer_list)

for item in customer_list:
    print(item.id, item.name, item.cost)
