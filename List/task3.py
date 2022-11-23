n = int(input())
list = []
for i in range(n):
    k = int(input())
    list.append(k)
for i in range(n):
    if(list[i]<0):
        print(list[i])
for i in range(n):
    if(list[i]==0):
        print(list[i])
for i in range(n):
    if(list[i]>0):
        print(list[i])