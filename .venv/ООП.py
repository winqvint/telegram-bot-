class Student:
    course = "Data Science"
print(Student.__dict__) #Проверка создан ли атрибут

s1 = Student()
s1.name = "Иван"
s1.surname= "Иванов"
s1.semester= 1
(print(s1.__dict__)) #Повторная проверка установились ли новые атрибуты

result =  s1.__dict__
print(result) # Проверка выносится ли наш общий список