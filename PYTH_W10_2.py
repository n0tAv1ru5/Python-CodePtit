def Count(n, h):
    count = 0
    for i in range(1, n):
        if sum(map(int, list(str(i)))) == h:
            count += 1
    return count


while True:
    input_data = input()
    if input_data == "-1":
        break
    else:
        n, h = map(int, input_data.split())
        print(Count(n, h))
