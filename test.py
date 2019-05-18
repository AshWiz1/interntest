str = "UDUD"
len = 4
level,count = 0,0
for i in range(len):
    if str[i] == 'D' :   level = level-1
    else :
        level = level+1
        if level == 0 :
            count = count+1
print(count)