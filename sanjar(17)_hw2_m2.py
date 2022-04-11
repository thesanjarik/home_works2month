class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Jack(Person):

    def __init__(self,  first_name, last_name, phone_number, balance,):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance

class Vito(Jack):
    _balance = 100
    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name, phone_number, balance)

    # def _get_balance(self):
    #     print(self._balance)

    def Balance(self, ):
        p = self._balance - 50
        d = self.balance + p
        self.balance = d
        print(self.balance)


g = Vito("oik", "jack", 12345678, 40)
g.Balance()
g.Balance()
g.Balance()
g.Balance()
g.Balance()
g.Balance()
