import unittest
from eisenstein import EisensteinInt

class EisensteinIntTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(EisensteinInt(1,0) + EisensteinInt(1,0), EisensteinInt(2,0))
        self.assertEqual(EisensteinInt(1,-1) + EisensteinInt(1,-1), EisensteinInt(2,-2))

    def test_mult(self):
        self.assertEqual(EisensteinInt(1,0) * EisensteinInt(1,0), EisensteinInt(1,0))
        self.assertEqual(EisensteinInt(10,0) * EisensteinInt(-1,0), EisensteinInt(-10,0))
        self.assertEqual(EisensteinInt(3,1) * EisensteinInt(2,-1), EisensteinInt(7,0))

    def test_sub(self):
        self.assertEqual(EisensteinInt(1,0) - EisensteinInt(1,0), EisensteinInt(0,0))
        self.assertEqual(EisensteinInt(1,-1) - EisensteinInt(1,-1), EisensteinInt(0,0))
        self.assertEqual(EisensteinInt(10,-1) - EisensteinInt(1,12), EisensteinInt(9,-13))
        self.assertEqual(EisensteinInt(5,-1) - EisensteinInt(10,-10), EisensteinInt(-5,9))

    def test_is_prime(self):
        # Test whether a number is an Eisenstein prime
        self.assertTrue(EisensteinInt(1,-1).is_prime())
        self.assertTrue(EisensteinInt(2,0).is_prime())
        self.assertTrue(EisensteinInt(2,1).is_prime())
        self.assertTrue(EisensteinInt(1,2).is_prime())
        self.assertTrue(EisensteinInt(-2,-1).is_prime())
        self.assertTrue(EisensteinInt(-3,1).is_prime())
        self.assertFalse(EisensteinInt(-2,-2).is_prime())
        self.assertFalse(EisensteinInt(1,0).is_prime())
        self.assertFalse(EisensteinInt(3,0).is_prime())
        self.assertFalse(EisensteinInt(7,0).is_prime())

    def test_units(self):
        # Test that units are generated
        units = EisensteinInt.units()
        self.assertEqual(EisensteinInt(1,0), units[0])
        self.assertEqual(EisensteinInt(1,1), units[1])
        self.assertEqual(EisensteinInt(0,1), units[2])
        self.assertEqual(EisensteinInt(-1,0), units[3])
        self.assertEqual(EisensteinInt(-1,-1), units[4])
        self.assertEqual(EisensteinInt(0,-1), units[5])

    def test_conjugate(self):
        self.assertEqual(EisensteinInt(0,1).conjugate(), EisensteinInt(-1,-1))
        self.assertEqual(EisensteinInt(1,0).conjugate(), EisensteinInt(1,0))
        self.assertEqual(EisensteinInt(3,1).conjugate(), EisensteinInt(2,-1))

    def test_norm_for_units(self):
        # Norm of units are 1
        self.assertEqual(EisensteinInt(1,0).norm(), 1)
        self.assertEqual(EisensteinInt(-1,0).norm(), 1)
        self.assertEqual(EisensteinInt(0,1).norm(), 1)
        self.assertEqual(EisensteinInt(0,-1).norm(), 1)
        self.assertEqual(EisensteinInt(-1,-1).norm(), 1)
        self.assertEqual(EisensteinInt(1,1).norm(), 1)
        self.assertEqual(EisensteinInt(-2,-2).norm(), 4)
        self.assertEqual(EisensteinInt(1,-1).norm(), 3)

    def test_norm_multiplicative(self):
        # Norm(a)*Norm(b)=Norm(a*b)
        a = EisensteinInt(-2,4)
        b = EisensteinInt(1,3)
        self.assertEqual((a * b).norm(), a.norm() *b.norm())

    def test_norm_and_conjugate(self):
        # a * a.conjugate = norm(a)
        a = EisensteinInt(3,1)
        aa = a * a.conjugate()
        norm = a.norm()
        self.assertTrue(aa.real == norm)

        a = EisensteinInt(13,-21)
        aa = a * a.conjugate()
        norm = a.norm()
        self.assertTrue(aa.real == norm)

    def test_is_even(self):
        # Even iff. norm congruent to 0 mod 3
        # Not even iff. norm congruent to 1 mod 3
        self.assertTrue(EisensteinInt(1,-1).is_even())
        self.assertTrue(EisensteinInt(1,-1).norm() % 3 == 0)

        self.assertFalse(EisensteinInt(5,2).is_even())
        self.assertTrue(EisensteinInt(5,2).norm() % 3 == 1)

        self.assertFalse(EisensteinInt(5,8).is_even())

    def test_str(self):
        self.assertEqual(str(EisensteinInt(1,0)), "1")
        self.assertEqual(str(EisensteinInt(0,0)), "0")
        self.assertEqual(str(EisensteinInt(1,1)), "1 + ω")
        self.assertEqual(str(EisensteinInt(1,-1)), "1 - ω")
        self.assertEqual(str(EisensteinInt(1,-2)), "1 - 2ω")
        self.assertEqual(str(EisensteinInt(-1,-2)), "-1 - 2ω")
        self.assertEqual(str(EisensteinInt(-1,2)), "-1 + 2ω")
        self.assertEqual(str(EisensteinInt(0, 1)), "ω")
        self.assertEqual(str(EisensteinInt(1,2)), "1 + 2ω")
        self.assertEqual(str(EisensteinInt(2,0)), "2")
        self.assertEqual(str(EisensteinInt(-2,0)), "-2")

    def test_associates(self):
        associates = EisensteinInt(2,1).associates()
        self.assertEqual(EisensteinInt(2,1), associates[0])
        self.assertEqual(EisensteinInt(1,2), associates[1])
        self.assertEqual(EisensteinInt(-1,1), associates[2])
        self.assertEqual(EisensteinInt(-2,-1), associates[3])
        self.assertEqual(EisensteinInt(-1,-2), associates[4])
        self.assertEqual(EisensteinInt(1,-1), associates[5])

    def test_complex_to_eisenstein(self):
        a = EisensteinInt(3,5)
        c = a.complex_form()
        e = EisensteinInt.eisenstein_form(c)
        self.assertEqual(a,e)

        a = EisensteinInt(-3,-2)
        c = a.complex_form()
        e = EisensteinInt.eisenstein_form(c)
        self.assertEqual(a,e)

        a = EisensteinInt(-2,3)
        c = a.complex_form()
        e = EisensteinInt.eisenstein_form(c)
        self.assertEqual(a,e)

        a = EisensteinInt(2,-5)
        c = a.complex_form()
        e = EisensteinInt.eisenstein_form(c)

        self.assertEqual(a,e)

    def test_conjugate_is_prime(self):
        self.assertTrue(EisensteinInt(-3,1).is_prime())
        self.assertTrue(EisensteinInt(-3,1).conjugate().is_prime())
        self.assertTrue(EisensteinInt(1,-1).is_prime())
        self.assertTrue(EisensteinInt(1,-1).conjugate().is_prime())

    def test_gt_and_lt(self):
        a = EisensteinInt(2,0)
        b = EisensteinInt(1,0)
        self.assertTrue(a > b)
        self.assertTrue(b < a)

        a = EisensteinInt(-3,-4)
        b = EisensteinInt(1,-1)
        self.assertTrue(a > b)
        self.assertTrue(b < a)

    def test_floor_div_identity(self):
        a=EisensteinInt(1,-1)
        self.assertEqual(a // a, EisensteinInt(1))
        a=EisensteinInt(1,10)
        self.assertEqual(a // a, EisensteinInt(1))
        a=EisensteinInt(-2,-4)
        self.assertEqual(a // a, EisensteinInt(1))
        a=EisensteinInt(-5,1)
        self.assertEqual(a // a, EisensteinInt(1))

    def test_floor_div_ints(self):
        a=EisensteinInt(10,0)
        b=EisensteinInt(7,0)
        self.assertEqual(a // b , EisensteinInt(1,0))

        a=EisensteinInt(17,0)
        b=EisensteinInt(9,0)
        self.assertEqual(a // b , EisensteinInt(2,0))

        a=EisensteinInt(10,0)
        b=EisensteinInt(5,0)
        self.assertEqual(a // b, EisensteinInt(2,0))

        a=EisensteinInt(20,0)
        b=EisensteinInt(-10,0)
        self.assertEqual(a // b , EisensteinInt(-2,0))

        a=EisensteinInt(-20,0)
        b=EisensteinInt(-10,0)
        self.assertEqual(a // b , EisensteinInt(2,0))

        a=EisensteinInt(-20,0)
        b=EisensteinInt(10,0)
        self.assertEqual(a // b , EisensteinInt(-2,0))

    def test_floor_div(self):
        a=EisensteinInt(8,0)
        b=EisensteinInt(3,1)
        self.assertEqual(a // b , EisensteinInt(2,-1))


    def test_divmod(self):
        a=EisensteinInt(3,1) # 3 + w
        b=EisensteinInt(2, -1) # 3 + w**2
        r1=EisensteinInt(1,0)
        d=(a*b)+r1

        q,r2 = divmod(d, a)
        self.assertTrue(q == b)
        self.assertTrue(r1 == r2)

        a=EisensteinInt(3,21)
        b=EisensteinInt(-34, -1)
        r1=EisensteinInt(1,0)
        d=(a*b)+r1

        q,r2 = divmod(d, a)
        self.assertTrue(r1 == r2)
        self.assertTrue(q == b)

        a=EisensteinInt(-3,21)
        b=EisensteinInt(-5, -1)
        r1=EisensteinInt(1,0)
        d=(a*b)+r1

        q,r2 = divmod(d, a)
        self.assertTrue(r1 == r2)
        self.assertTrue(q == b)

        a=EisensteinInt(19,2)
        b=EisensteinInt(3, -2)
        r1=EisensteinInt(2,1)
        d=(a*b)+r1

        q,r2 = divmod(d, a)
        self.assertTrue(q == b)
        self.assertTrue(r1 == r2)

        a=EisensteinInt(-1,-3)
        b=EisensteinInt(-5, -1)
        r1=EisensteinInt(1,0)
        d=(a*b)+r1

        q,r2 = divmod(d, a)
        self.assertTrue(q == b)
        self.assertTrue(r1 == r2)

        a=EisensteinInt(-3,21)
        b=EisensteinInt(5, -1)
        r1=EisensteinInt(1,0)
        d=(a*b)+r1

        q,r2 = divmod(d, a)
        self.assertTrue(r1 == r2)
        self.assertTrue(q == b)

    def test_gcd_ints(self):
        a=EisensteinInt(12,0)
        b=EisensteinInt(6,0)
        self.assertEqual(a.gcd(b).canonical(), EisensteinInt(6,0).canonical())

        a=EisensteinInt(20,0)
        b=EisensteinInt(12,0)
        self.assertEqual(a.gcd(b).canonical(), EisensteinInt(-4,0).canonical())

        a=EisensteinInt(5,0)
        b=EisensteinInt(7,0)
        self.assertEqual(a.gcd(b).canonical(), EisensteinInt(1,0).canonical())

    def test_gcd(self):
        p=EisensteinInt(3,1)
        q=EisensteinInt(1,-1)
        r=EisensteinInt(2,-1)

        assert(p.is_prime())
        assert(q.is_prime())
        assert(r.is_prime())

        a=p*q
        b=p*r

        self.assertEqual(a.gcd(b).canonical(),p.canonical())

        p=EisensteinInt(-4,-1)
        q=EisensteinInt(2,0)
        r=EisensteinInt(6,1)

        assert(p.is_prime())
        assert(q.is_prime())
        assert(r.is_prime())

        a=p*q
        b=p*r

        self.assertEqual(a.gcd(b).canonical(),p.canonical())

        p=EisensteinInt(3,2)
        q=EisensteinInt(-1,3)
        r=EisensteinInt(9,1)

        assert(p.is_prime())
        assert(q.is_prime())
        assert(r.is_prime())

        a=p*q
        b=p*r

        self.assertEqual(a.gcd(b).canonical(),p.canonical())



if (__name__ == '__main__'):
    unittest.main()
