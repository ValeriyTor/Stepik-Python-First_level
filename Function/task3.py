# объявление функции
def print_digit_sum(num):
    result = 0
    list = [ int(i) for  i  in  str(num) ]
    result = sum(list)
    print(result)
    
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)