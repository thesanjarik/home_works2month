class Fraction:
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def __add__(self, other):
        print(self.numerator + self.denumerator)
        return self.numerator + self.denumerator

    def __sub__(self, other):
        print(self.numerator + self.denumerator)
        return self.numerator + self.denumerator

    def __truediv__(self, other):
        print(self.numerator / self.denumerator)
        return self.numerator / self.denumerator

    def __mul__(self, other):
        print(self.numerator * self.denumerator)
        return self.numerator * self.denumerator

num = Fraction(10, 10)
num * 1






