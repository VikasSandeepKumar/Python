class AreaRect:

    def __init__(self, l, b):
        self.l=l
        self.b=b

    def calculate_area(self):
        return self.l * self.b

area1 = AreaRect(5, 8)
area2 = AreaRect(76, 67)
print(area1.calculate_area())
print(area2.calculate_area())