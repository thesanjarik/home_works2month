
class Car:
    def __init__(self, title, model, weight,  max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        car1 = str(self.title) + '' + self.model
        return car1.upper()

    def stop_engine(self):
        car2 = str(self.title) + 'engine stopped!' + self.model
        return car2.upper()

    def all_info(self):
        print(f"""
               name:{self.title}
                age:{self.model}
                weight:{self.weight} 
                max_speed: {self.max_speed}
                color: {self.color}
                """)

toyota = Car(' BMW ', ' e34 ', 100.0, 120, 'red')
print(toyota.start_engine())

print(toyota.stop_engine())

toyota.all_info()







