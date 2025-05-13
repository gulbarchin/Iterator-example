#Функция-итератор

my_list = [1,2,3,4]
#for i in my_list:
#   print(i)

iterator = iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Эту функцию мы можем сделать с помощью while
iterator = iter(my_list)
try:
    while True:
        element = next(iterator)
        print(element)
except StopIteration:
    print('The end')


