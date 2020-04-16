from sympy import isprime, primefactors, factorint, solve, symbols, Symbol, Eq
from math import sqrt, pi, sin, cos, atan
import matplotlib.pyplot as plt
import numpy as np

class EisensteinInt:
    """
    Stores the Eisenstein integer in the form a + bω

    Create Eisenstein Integer by:
	     a = EisensteinInt(5,7)  # Create (5 + 7ω)
	     a = EisensteinInt(13)  # Create (13 + 0ω)

    Functions implemented
         Basic functions: init(), ==, hash(),  str(),
	     Arithmetic functions: abs(), +, divmod(), //, %, *, -

         a.associates() - Returns a list of the product of the number and
            each of the units.
         a.complex_form() - Returns the complex form.
         a.conjugate() - Returns an EisensteinInt representing he conjugate.
         a.norm() - Returns an integer representing the norm.
         a.polar_form() - Returns a tuple of the radius and angle.
         EisensteinInt.units() - Returns a list of the 6 Eisenstein units

         a.is_even() - Returns whether or not n is even.
         a.is_prime() - Returns whether or not n is a prime.
         a.is_unit() - Returns whether or not n is a unit.

         a.gcd(b) - Compute the greatest common divisor of a and b.
         a.plot_point() - Plots a single point in a polar plane.
         a.plot_multiples(n,labels) - Plots the multipls of the number n
            degrees out and gives the option to include labels.
         a.get_multiples(n) - Returns a list of multiples n degrees away
         EisensteinInt.plot_all(n,prime) - Plots all Eisenstein integers
            and can highlight the prime numbers
         EisensteinInt.generate_eisenstein_ints(n) - Generates all EisensteinInt
            and their multiples through brute force
    """

    def __init__(self, real=0, imaginary=0):
        assert isinstance(real, int)
        assert isinstance(imaginary, int)

        self.real = real
        self.imaginary = imaginary

    def __hash__(self):
        return hash((self.real, self.imaginary))

    def __eq__(self, other):
        if isinstance(other, EisensteinInt):
            return (self.real == other.real) and (self.imaginary == other.imaginary)
        else:
            return False

    def __str__(self):
        a = self.real
        b = self.imaginary

        result = "{r} + {i}ω".format(r=str(a), i=str(b))
        return result

    def debug_str(self):
        result = "EisensteinInt({}, {})".format(self.real, self.imaginary)
        return result

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

        # Offset flooring with a negative
        if (nr <0):
            quotient_real += 1
        if (ni <0):
            quotient_imaginary += 1

        quotient = EisensteinInt(quotient_real, quotient_imaginary)

        return quotient

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

    def associates(self):
        units = EisensteinInt.units()
        associates = list(map(lambda x: x * self, units))
        return associates

    def complex_form(self):
        r = self.real
        i = self.imaginary

        real =  r + (i * (-1/2))
        imag = (i * sqrt(3)) / 2

        return complex(real, imag)

    def conjugate(self):

        a = self.real
        b = self.imaginary

        conjugate_real = a-b
        conjugate_imag = -b
        return EisensteinInt(conjugate_real, conjugate_imag)

    def norm(self):
        # Norm(a) = a^2 - ab + b^2

        a = self.real
        b = self.imaginary
        norm = a**2 - a*b + b**2
        return norm

    def polar_form(self):
        r = abs(self)

        a = self.real
        b = self.imaginary

        x = ((2*a -b)/2)* sqrt(3)
        y = b*3/2

        if x == 0 and y >0:
            angle = pi/2
        elif x == 0 and y <0:
            angle = -1 * pi/2
        elif x == 0 and y == 0:
            angle = 0
        else:
            angle = atan(y/x)

        if (x < 0):
            if (y != 0):
                angle = angle + pi
            else:
                angle = np.pi - angle

        return (r, angle)

    @staticmethod
    def units():
        units = []
        unit = EisensteinInt(1,0)
        for i in range(6):
            units.append(unit)
            unit = unit * EisensteinInt(1, 1)
        return units

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

    def is_unit(self):
        if (self.norm() == 1):
            return True
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

    def plot_point(self):
        max_len = 0

        length, angle = self.polar_form()

        if (length > max_len):
            max_len = length

        r = self.real
        i = self.imaginary

        plt.polar(angle, length, 'ro')
        plt.text(angle, length, '%d + %dω' % (int(r), int(i)), horizontalalignment='center', verticalalignment='bottom')

        plt.thetagrids(range(0, 360, 60), ('1', '1+ω', 'ω', '-1', '-ω-1', '-ω'))
        plt.rgrids(np.arange(0,max_len,max_len/10), labels=[])

        plt.show()
        return plt

    def plot_multiples(self, n=2, labels=True):
        max_len = 0

        multiples = self.get_multiples(n)

        for multiple in multiples:
            length, angle = multiple.polar_form()

            if (length > max_len):
                max_len = length

            r = multiple.real
            i = multiple.imaginary

            if multiple == self:
                plt.polar(angle, length, 'ro')
            else:
                plt.polar(angle, length, 'bo')
            if (labels):
                plt.text(angle, length, '%d + %dω' % (int(r), int(i)), horizontalalignment='center', verticalalignment='bottom')

        plt.thetagrids(range(0, 360, 60), ('1', '1+ω', 'ω', '-1', '-ω-1', '-ω'))
        plt.rgrids(np.arange(0,max_len,max_len/10), labels=[])

        plt.show()

        return plt

    def get_multiples(self, n):
        units = EisensteinInt.units()

        multiples = units
        for i in range(1, n):
            multiples = self.__find_multiples(multiples, units)
        multiples = list(map(lambda x: x * self,multiples))
        return multiples

    def __find_multiples(self, multiples, units):
        # Private helper function
        rv = set()
        for i in multiples:
            for j in units:
                val = i + j
                if (val != EisensteinInt(0, 0)):
                    rv.add(val)

        return rv

    @staticmethod
    def plot_list(points, primes=False, labels=False):
        max_len = 0
        for pt in points:
            length, angle = pt.polar_form()

            if (length > max_len):
                max_len = length

            r = pt.real
            i = pt.imaginary

            if pt.is_prime():
                plt.polar(angle, length, 'ro')
            else:
                plt.polar(angle, length, 'bo')
            if (labels):
                plt.text(angle, length, '%d + %dω' % (int(r), int(i)), horizontalalignment='center', verticalalignment='bottom')

        plt.thetagrids(range(0, 360, 60), ('1', '1+ω', 'ω', '-1', '-ω-1', '-ω'))
        plt.rgrids(np.arange(0,max_len,max_len/10), labels=[])

        plt.show()

        return plt

    @staticmethod
    def plot_all(n=4, prime=False):
        ei = EisensteinInt.generate_eisenstein_ints(n)
        EisensteinInt.plot_list(ei, prime)

    @staticmethod
    def generate_eisenstein_ints(n):
        min_real = -1 * n
        min_imag = -1 * n
        max_real = n
        max_imag = n

        eis = set()
        for r in range(min_real, max_real):
            for i in range(min_imag, max_imag):
                ei = EisensteinInt(r, i)
                multiples = ei.get_multiples(n)
                for m in multiples:
                    eis.add(m)
                eis.add(ei)
        return eis

    def divide_by_prime(self, prime):
        conjugate = prime.conjugate()

    # def factor():

#     def factors(self):
#         if(self.is_prime()):
#             return [self]
#
#         norm = self.norm()
#
#         norm_factors = primefactors(norm)
#         for i in norm_factors:
#             print(i)
#         return []
#
#     def divide_by_three(self):
#
    # def generate_random_prime():
# a = EisensteinInt(5)
# b = EisensteinInt(13)
# c = EisensteinInt(1, -1) * EisensteinInt(3, 2)
# f = a.factors()
#
# # for i in f:
# #     print(i.debug_str())
# #
# # f = b.factors()
# # for i in f:
# #     print(i.debug_str())
#
# x = symbols('x')
# y = symbols('y')
# p =3
# expr = x**2 - x*y + y** 2
# eq = Eq(expr, p);
# print(solve(eq,x, y, dict=True))

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
