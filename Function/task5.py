# объявление функции
def find_all(target, symbol):
    list = []
    for i in range(len(target)):
        if target[i]==symbol:
            list.append(i)
    return list
# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))