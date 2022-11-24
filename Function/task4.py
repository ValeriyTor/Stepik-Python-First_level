# объявление функции
def get_factors(num):
    list = []
    for i in range(1,num+1):
        if(n % i == 0):
            list.append(i)
    return list
# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))