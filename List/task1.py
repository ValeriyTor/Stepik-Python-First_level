n = int(input())
list = []
for i in range(n):
    k = int(input())
    list.append(k)
print(*list,sep="\n")
print("")
for i in range(len(list)):
    print((list[i]**2+2*list[i]+1),sep="\n")