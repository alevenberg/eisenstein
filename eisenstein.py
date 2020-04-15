from sympy import isprime

class EisensteinInt:

    """
    Stores the Eisenstein integer in the form a + bω
    Create Eisenstein Integer by:
	     n = GaussInt(5,7)  # Create (5 + 7ω)
	     n = GaussInt(13)  # Create (13 + 0ω)
    Functions implemented
	     Arithmetic functions: +, -, *, //
         Basic functions: init(), ==, str()
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

    def __divmod__(self, other):

        divisor = other

        quotient = self//divisor
        p = other*quotient
        remainder = self - p

        return quotient, remainder

    def __mod__(self, other):
        q, r = divmod(self, other)
        return r

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



    def get_complex_form(self):
        r = self.real
        i = self.imaginary

        real =  r - (i/2)
        imag = (i * sqrt(3)) / 2

        return complex(real, amg)

    def get_eisenstein_form(c):
        real = c.real
        imag = c.imag

        eisenstein_real = real + (1//sqrt(3)) * imag
        eisenstein_imag = (2//sqrt(3)) * imag

        return EisensteinInt(eisenstein_real, eisenstein_imag)




# a = EisensteinInt(10,4)
# b = EisensteinInt(1,2)
# unit = EisensteinInt(2,1)
#
# mult = a*b
# add = a+b
# sub = a-b
# norm = a.norm()
# gcd = a.gcd(b)

# c = complex(1,2)
# print("Mult:", mult)
# print("Sub:", sub)
# print("Add:", add)
# print("Norm:", norm)
# print("gcd:", gcd)

# print("unit:", unit.is_unit())
# print("unit:", a.is_unit())

# print("prime:", a.is_prime())
# print("prime:", b.is_prime())
# print("prime:", unit, unit.is_prime())

# Sources
# http://math.bu.edu/people/jsweinst/Teaching/MA341Spring18/MA341Notes.pdf
# https://proofwiki.org/wiki/Norm_of_Eisenstein_Integer
# https://arxiv.org/pdf/1602.09106.pdf
# https://doi.org/10.1016/j.jsc.2004.02.006
# https://en.wikipedia.org/wiki/Eisenstein_integer
# http://hackage.haskell.org/package/arithmoi-0.8.0.0/docs/Math-NumberTheory-Quadratic-EisensteinIntegers.html
# https://thekeep.eiu.edu/cgi/viewcontent.cgi?article=3459&context=theses
# https://mathworld.wolfram.com/EisensteinPrime.html
