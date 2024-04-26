with open("VANBAN.in", "r") as file:
    rev_string = ""
    count = 0
    lines = file.readlines()
    for line in lines:
        for word in line.split(): 
            if word == word[::-1] and len(word) > len(rev_string):  
                rev_string = word
                count = 1 
            elif word == rev_string:
                count += 1  
    print(rev_string, count)
