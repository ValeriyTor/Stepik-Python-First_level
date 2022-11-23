s = input()
counter1 = 0
counter2 = 0
for i in range(len(s)):
    if(s[i] == "+"):
        counter1+=1
    if(s[i] == "*"):
        counter2+=1
print("Symbol + meets", counter1)
print("Symbol * meets", counter2)