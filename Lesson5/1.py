class Complex:
    re = 'Value re'
    im = 'Value im'

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, a):
        temp = Complex(self.re, self.im)
        temp.re += a.re
        temp.im += a.im
        return temp

    def __sub__(self, a):
        temp = Complex(self.re, self.im)
        temp.re -= a.re
        temp.im -= a.im
        return temp

    def __mul__(self, a):
        temp = Complex(self.re, self.im)
        temp.re = self.re * a.re - self.im * a.im
        temp.im = self.im * a.re + a.im * self.re
        return temp

    def __truediv__(self, a):
        temp = Complex(self.re, self.im)
        temp.re = (self.re * a.re + self.im * a.im) / a.cabs()
        temp.im = (self.im * a.re - a.im * self.re) / a.cabs()
        return temp

    def cabs(self):
        return (self.re * self.re + self.im * self.im) ** (0.5)

    def __str__(self):
        if (self.im >= 0):
            return ("%.2f+%.2fi" % (self.re, self.im))
        else:
            return ("%.2f%.2fi" % (self.re, self.im))

    pass


c = Complex(float(input()), float(input()))
d = Complex(float(input()), float(input()))

print(c + d)
print(c - d)
print(c * d)
print(c / d)
print("%.2f" % c.cabs())
print("%.2f" % d.cabs())
