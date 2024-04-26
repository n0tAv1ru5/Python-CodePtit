class receipt:
    def __init__(self, code, name, brand, number, price, discount):
        self.code = code
        self.name = name
        self.brand = brand
        self.price = price
        self.discount = discount
        self.number = number
        self.total = number * price - discount

    def __lt__(self, other):
        if self.total == other.total:
            return self.code < other.code
        return self.total > other.total


receipt_list = list()
for i in range(int(input())):
    code = input()
    type_brand = input().split()
    name, brand = " ".join(type_brand[:-1]), type_brand[-1]
    number = int(input())
    price = int(input())
    discount = int(input())
    receipt_list.append(receipt(code, name, brand, number, price, discount))

receipt_list.sort()

for receipt in receipt_list:
    print(
        receipt.code,
        receipt.name,
        receipt.brand,
        receipt.number,
        receipt.price,
        receipt.discount,
        receipt.total,
    )
