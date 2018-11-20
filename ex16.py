class Fraction(object):
        def __init__(self,num,denum):

            self.num = num;
            self.denum = denum;

        def __str__(self):
            return str(self.num)+"/"+str(self.denum)

        def __add__(self,other):
            add1 = self.num * other.denum + self.denum * other.num
            add2 = self.denum * other.denum
            return Fraction(add1,add2)


Fraction1 = Fraction(2,3)
Fraction2 = Fraction(1,4)
Fraction3 = Fraction1+Fraction2
print(Fraction3)
