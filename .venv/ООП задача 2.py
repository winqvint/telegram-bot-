class Group:
    members = []

class Student:
    course = "Data Science"


s1 = Student()
s1.name = "Иван"
s1.surname= "Иванов"
s1.semester= 1

s2 = Student()
s2.name = "Лев"
s2.surname = "Сергеев"
s2.semester = 1

Group.members.append(s1)
Group.members.append(s2)



result = Group.members
