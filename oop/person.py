class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}'s age: {self.age}"

    def greeting(self):
        print("Hello my name is " + self.name)


me = Person('Long', 23)

print(me)
me.greeting()
