from sympy import isprime
from math import sqrt, pi, sin, cos
from cmath import polar
import matplotlib.pyplot as plt
import numpy as np

class EisensteinInt:
    """
    Stores the Eisenstein integer in the form a + bω
    Create Eisenstein Integer by:
	     n = GaussInt(5,7)  # Create (5 + 7ω)
	     n = GaussInt(13)  # Create (13 + 0ω)
    Functions implemented
         Basic functions: init(), ==, str()
	     Arithmetic functions: +, -, *, //, %, divmod()

         n.norm() - Returns the norm.
         n.conjugate() - Returns the conjugate.

         n.is_unit() - Returns whether or not n is a unit.
         n.is_even() - Returns whether or not n is even.
         n.is_prime() - Returns whether or not n is a prime.

         a.gcd(b) - Compute the greatest common divisor of a and b.
    """

    def __init__(self, real=0, imaginary=0):
        assert isinstance(real, int)
        assert isinstance(imaginary, int)

        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        result = "EisensteinInt({}, {})".format(self.real, self.imaginary)
        return result

    def __eq__(self, other):
        if isinstance(other, EisensteinInt):
            return (self.real == other.real) and (self.imaginary == other.imaginary)
        else:
            return False

    def __abs__(self):
        return sqrt(self.norm())

    def __add__(self, other):
        if isinstance(other, int):
            other = EisensteinInt(other)

        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary

        sum_real = a + c
        sum_imaginary = b + d

        return EisensteinInt(sum_real, sum_imaginary)

    def __divmod__(self, other):

        divisor = other

        quotient = self//divisor
        p = other*quotient
        remainder = self - p

        return quotient, remainder

    def __floordiv__(self, other):

        if isinstance(other, int):
            other = EisensteinInt(other)

        numerator = (self) * other.conjugate()
        denominator = other.norm()

        nr = numerator.real
        ni = numerator.imaginary

        quotient_real = nr // denominator
        quotient_imaginary = ni // denominator
        quotient = EisensteinInt(quotient_real, quotient_imaginary)

        return quotient

    def __sub__(self, other):
        if isinstance(other, int):
            other = EisensteinInt(other)

        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary

        difference_real = a - c
        difference_imaginary = b - d

        return EisensteinInt(difference_real, difference_imaginary)

    def __mod__(self, other):
        q, r = divmod(self, other)
        return r

    def __mul__(self, other):
        # (a+bω)*(c+dω)=(ac-bd)+(ad+b(c-d))ω

        if isinstance(other, int):
            other = EisensteinInt(other)

        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        product_real = (a*c)-(b*d)
        product_imaginary = (a*d)+b*(c-d)

        return EisensteinInt(product_real, product_imaginary)

    def norm(self):
        # Norm(a) = a^2 - ab + b^2

        a = self.real
        b = self.imaginary
        norm = a**2 - a*b + b**2
        return norm

    def conjugate(self):

        a = self.real
        b = self.imaginary

        conjugate_real = a-b
        conjugate_imag = -b
        return EisensteinInt(conjugate_real, conjugate_imag)

    def is_unit(self):
        if (self.norm() == 1):
            return True
        else:
            return False

    def is_even(self):
        # is_even iff. a+b is congruent to 0 mod 3

        a = self.real
        b = self.imaginary

        if (((a+b) % 3) == 0):
            return True
        else:
            return False

    def is_prime(self):
        # n is an eisenstein prime if
        # 1) b=0 and a=p, prime and p≡2 mod 3
        # 2) a=0 and b=p, prime and p≡2 mod 3
        # 3) Norm(n) = p is prime where p=3 or p≡1 mod 3

        a = self.real
        b = self.imaginary

        if (b == 0 and isprime(a) and (a % 3 == 2)):
            return True
        if (a == 0 and isprime(b) and (b % 3 == 2)):
            return True

        norm = self.norm()
        is_prime = isprime(norm)

        if (is_prime):
            # Norm == 3 is 1-ω
            return (norm == 3) or (norm % 3 == 1)
        else:
            return False

    def gcd(self, other):

        a = self
        b = other

        if (a.norm() < b.norm()):
            return b.gcd(a)

        while (b.norm() > 0):
            q, r = divmod(a, b)
            a, b = b, r

        return a

    def complex_form(self):
        r = self.real
        i = self.imaginary

        real =  r + (i * (-1/2))
        imag = (i * sqrt(3)) / 2

        return complex(real, imag)

    def polar_form(self):
        radius, phi = polar(a.complex_form())
        # phi = phi * 180 /pi # To debug: turn into degree

        r = abs(self)
        assert(radius == r)

        return (polar(a.complex_form()))

    # def plot_multiples(self):



    def plot_point(self):
        length, angle = self.polar_form()
        # Angle in radians
        # x = length * cos(angle)
        # y = length * sin(angle)

        r = self.real
        i = self.imaginary

        plt.polar(angle, length, 'ro')
        plt.text(angle, length, '%d + %dω' % (int(r), int(i)), horizontalalignment='center', verticalalignment='bottom')

        plt.thetagrids(range(0, 360, 60), ('1', '1+ω', 'ω', '-1', '-ω-1', '-ω'))
        plt.rgrids(np.arange(0,length + 1,1), labels=[])

        plt.show()

a = EisensteinInt(1, -2)
# a = EisensteinInt(1, 1)
r, phi = polar(a.complex_form())
phi = phi * 180 /pi
radius = abs(a)
a.plot_point()
print(r, radius, phi)
# Sources
# http://math.bu.edu/people/jsweinst/Teaching/MA341Spring18/MA341Notes.pdf
# https://proofwiki.org/wiki/Norm_of_Eisenstein_Integer
# https://arxiv.org/pdf/1602.09106.pdf
# https://doi.org/10.1016/j.jsc.2004.02.006
# https://en.wikipedia.org/wiki/Eisenstein_integer
# http://hackage.haskell.org/package/arithmoi-0.8.0.0/docs/Math-NumberTheory-Quadratic-EisensteinIntegers.html
# https://thekeep.eiu.edu/cgi/viewcontent.cgi?article=3459&context=theses
# https://mathworld.wolfram.com/EisensteinPrime.html
# https://stackoverflow.com/questions/28417604/plotting-a-line-from-a-coordinate-with-and-angle
