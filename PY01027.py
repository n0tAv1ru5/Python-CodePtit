n = input()
check = {"6", "8"}
if not set(n) <= check or n[0] == "8" or "888" in n:
    print("NO")
else:
    print("YES")