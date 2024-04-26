def quat(input_bin):
    ans = ""
    if len(input_bin) % 2 != 0:
        input_bin = "0" + input_bin
    i = 0  
    while i < len(input_bin):
        ans += str(int(input_bin[i:i + 2], 2))   
        i += 2 
    return int(ans) 

for _ in range(int(input())):
    
    num_type = int(input())
    input_bin = input()
    
    if num_type == 4:
        print(quat(input_bin))
    elif num_type == 10:
        print(int(input_bin,2))
    elif num_type == 8:
        print(oct(int(input_bin,2))[2:])
    elif num_type == 16:
        print(hex(int(input_bin,2))[2:])
    else:
        print(input_bin)
