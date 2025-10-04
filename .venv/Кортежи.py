family = ('Вика', 'Маргарита ', 'Бронислав ', 'Григорий')
print( family[0], family[-1])
print(family[1::2])
numbers={1,3,5,6,78,33,5,7,7}
numbers_new = int(input('Введите новое значение множества '))
if numbers_new in numbers:
    numbers.remove(numbers_new)
else:
    numbers.add(numbers_new)
print(numbers, len(numbers))