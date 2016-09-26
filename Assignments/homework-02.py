"""
Name: Chris Cook
Email: c.w.cook@live.com
Assignment: Homework 2 - Fraction Class
Due: 26 Sep @ 1:00 p.m.
"""

class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d

    
    def gcd(self,a,b):
        z=self.numerator
        while b:
            a, b = b, a%b
        return a

    def __str__(self):
        mix = 0
        n = self.numerator
        d = self.denominator

        if (n>d):
            #holds the gcd
            gcdtmp = self.gcd(n,d)
            
            mix = int(n/d)
           
            n = (n-(d*mix))

            #recalculates the gcd with the new numerator
            gcdtmp = self.gcd(n,d)

            n = int(n/gcdtmp)

            d = int(d/gcdtmp)

            if n ==0:
                return "%s" % (mix)
            
            
            return "%s %s / %s" % (mix, n, d)
        else:
             return "%s / %s" % (n, d)    

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)
       
    def __add__(self,other):
    	x = (self.numerator*other.denominator)+(other.numerator*self.denominator)
    	y = (self.denominator*other.denominator)
    	return fraction(x,y)


if __name__ == '__main__':
    a = fraction(89,2)
    b = fraction(670,5)
    c = a + b
    print(a, end=" + ")
    print(b,end=" = ")
    print(c)