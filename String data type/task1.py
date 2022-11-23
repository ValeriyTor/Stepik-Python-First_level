s = input()
flag = True
for i in range(len(s)):
    if s[i] in '0123456789':
        print("Number")
        flag = True
        break
    else:
        flag = False
if(flag == False):
        print("String without numbers")