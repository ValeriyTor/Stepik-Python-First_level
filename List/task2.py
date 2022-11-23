n = int(input())
list = []
for i in range(n):
    k = input()
    list.append(k)
str = input()
for i in range(n):
    if(str.lower() in list[i].lower()):
        print(list[i])