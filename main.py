# Функция-генератор

def get_list():
    for x in [1,2,3,4]:
        yield x

a = get_list()
print(next(a))
print(next(a))
print(next(a))
print(next(a))


#Функция-итератор



