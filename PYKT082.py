def switch(n):
    if 3 <= n <= 4:
        return 2.5
    elif 5 <= n <= 6:
        return 3.0
    elif 7 <= n <= 9:
        return 3.5
    elif 10 <= n <= 12:
        return 4.0
    elif 13 <= n <= 15:
        return 4.5
    elif 16 <= n <= 19:
        return 5.0
    elif 20 <= n <= 22:
        return 5.5
    elif 23 <= n <= 26:
        return 6.0
    elif 27 <= n <= 29:
        return 6.5
    elif 30 <= n <= 32:
        return 7.0
    elif 33 <= n <= 34:
        return 7.5
    elif 35 <= n <= 36:
        return 8.0
    elif 37 <= n <= 38:
        return 8.5
    elif 39 <= n <= 40:
        return 9.0


for _ in range(int(input())):
    score_list = list(map(float, input().split()))

    average_score = (
        switch(score_list[0]) + switch(score_list[1]) + score_list[2] + score_list[3]
    ) / 4

    dec_part = average_score - int(average_score)

    if  dec_part < 0.25:
        average_score = float(int(average_score))
    elif 0.25 <= dec_part < 0.75:
        average_score = int(average_score) + 0.5
    elif  dec_part >= 0.75:
        average_score = int(average_score) + 1.0
    print(average_score)
