from person import Person


class Employee(Person):
    def __init__(self, name, age, skill):
        super().__init__(name, age)
        self.skill = skill

    def getInfo(self):
        print('Employee {}({}) has skill: {}'.format(
            self.name, self.age, self.skill))


e1 = Employee('Tony', 52, 'Rich')
e1.getInfo()
