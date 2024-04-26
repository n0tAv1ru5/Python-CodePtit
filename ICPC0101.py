stack = list()
input()
nums_list = list(map(int, input().split()))
for num in nums_list:
    if stack and (stack[-1] + num) & 1 == 0:
        stack.pop()
    else:
        stack.append(num)
print(len(stack))
