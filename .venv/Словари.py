phone_book = {'Мама': '+79165135756', 'Папа':'+79166914247','Вика':'+79151402388', 'Гриша': '+79152892731'}
print(phone_book.keys())
print(phone_book.values())
for key, value in phone_book.items():
    print(f'{key} - {value}')
phone_book['Тема']='+79137876308'
phone_book['Егорчик']='+79165191479'
phone_book['Егорчик'] = '+79165197865'
new_contact = input('Введите имя и телефон нового контакта:')
if new_contact in phone_book.keys():
    del phone_book[new_contact]
else:
    phone = input(('Введите телефон нового контакта:'))
    phone_book[new_contact] = phone
    print('Запись добавлена в контакты ')
print(phone_book)