
class Transport:
    def __init__(self, title, model, color):
        self.title = title
        self.model = model
        self.color = color

    def start_engine(self):
        print(f"Engine on {self.title} {self.model} started!")

class Car(Transport):
    def __init__(self, title, model, color, speed):
        super().__init__(title, model, color)
        self.speed = speed

class Airplane(Transport):

    def __init__(self, title, model, color, weight, height):
        super().__init__(title, model, color)
        self.weight = weight
        self.height = height

    def new_method(self):
        print("Its method in Airplane ")

class DeliveryAirplane(Airplane):

    def __init__(self, title, model, color, weight, height, amount):
        super().__init__(title, model, color, weight, height)
        self.amount = amount


bmw = Car('BMW', 'E34', 'black', 340)
bmw.start_engine()

boing = Airplane('Boing', 'x232', 'white', 10000, 5.5)
boing.start_engine()

boing.new_method()



