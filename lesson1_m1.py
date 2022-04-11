
class Transport:

    def __init__(self, title, model, type, year):
        self.title = title
        self.model = model
        self.type = type
        self.year = year

bmw = Transport('BMW', 'e34', 'car', 1990)
mercedes = Transport('Mercedes', 'w124', 'car', 1990)

class Dog:

    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def voice(self):
        print(f'{self.name} gaf! gaf!')

    def eat(self):
        print(f"{self.name} is eating meat!")

    def sleep(self):
        print(f"{self.name} wants sleep.....")

    def info(self, weight, height):
        print(f"""
        name:{self.name}
         age:{self.age}
         type:{self.type} 
         weight:{weight} 
         height: {height}
         """)
        self.weight = weight
        self.height = height


rex = Dog('Rex', 40, 'pitbull')
rex.voice()
rex.sleep()
rex.info(60, 1.70)

sharik = Dog('Sharik', 10, 'pitbull')
sharik.voice()
sharik.eat()

