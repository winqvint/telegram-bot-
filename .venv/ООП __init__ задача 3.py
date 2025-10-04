class Person:
    def __init__(self, name = None, age=None, gender = None, occupation = None ):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
    def set_attributes(self,attributes_dict):
        for attr_name, attr_value in attributes_dict.items():
            setattr(self,attr_name,attr_value)

    def show_card(self):
        print(f'Name: {self.name}'
              f'Age: {self.age}'
              f'Gender: {self.gender}'
              f'Occupation: {self.occupation}')