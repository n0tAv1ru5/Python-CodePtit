n = int(input())
quest_list = []
temp_list = []

for _ in range(n):
    try:
        line = input()
        if not line.strip():
            if temp_list:
                quest_list.append((temp_list[0], len(temp_list) - 1))
                temp_list = []
        else:
            temp_list.append(line)
    except EOFError:
        if temp_list:
            quest_list.append((temp_list[0], len(temp_list) - 1))
            temp_list = []

if temp_list:
    quest_list.append((temp_list[0], len(temp_list) - 1))

for title, count in quest_list:
    print(f"{title}: {count}")
