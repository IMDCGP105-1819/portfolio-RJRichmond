class Fraction(object):
        def __init__(self,num,denum):
            if type(num)!=int:
                raise Exception("The numerator of the fraction must be an int")
            if type(denum)!=int:
                raise Exception("The denominator of the fraction must be an int")
            self.num = num;
            self.denum = denum;

        def __str__(self):
            return str(self.num)+"/"+str(self.denum)

        def __add__(self,other):
            add1 = self.num * other.denum + self.denum * other.num
            add2 = self.denum * other.denum
            return Fraction(add1,add2)

        def __sub__(self,other):
            sub1 = self.num * other.denum - self.denum * other.num
            sub2 = self.denum * other.denum
            return Fraction(sub1,sub2)

        def __mul__(self,other):
            mul1 = self.num * other.num
            mul2 = self.denum * other.denum
            return Fraction(mul1,mul2)

        def __truediv__(self,other):
            flipped = Fraction(other.denum, other.num)
            return self * flipped

        def Inverse(self):
            return Fraction(self.denum, self.num)

Fraction1 = Fraction(2,3)
Fraction2 = Fraction(1,4)
Add = Fraction1+Fraction2
Sub = Fraction1-Fraction2
Mul = Fraction1*Fraction2
Div = Fraction1/Fraction2
Inv = Fraction1.Inverse()

print(Fraction1)
