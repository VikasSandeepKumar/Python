class RateOfInterest:
    interest = 0.06
    def __init__(self, name, loan):
        self.name = name
        self.loan = loan

    def calc_interest(self):
        print("Total interest: ", self.loan * self.interest)

# p1 = RateOfInterest("Vikas", 500000)
# p1.interest = 0.02
# p1.calc_interest()
#
# p2 = RateOfInterest("Dheeraj", 300000)
# p2.calc_interest()

class Student(RateOfInterest):
    interest = 0.04

s = Student("Vikas", 500000)
s.calc_interest()
