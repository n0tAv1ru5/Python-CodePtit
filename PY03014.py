from collections import deque

for _ in range(int(input())):

    stack = deque()
    ans = list()
    text_list = list(input())

    count = 0
    for char in text_list:
        if char == "(":
            count += 1
            stack.append(count)
            ans.append(count)
        if char == ")":
            ans.append(stack.pop())
    print(*ans)