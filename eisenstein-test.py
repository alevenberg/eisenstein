import unittest
from eisenstein import EisensteinInt

class EisensteinIntTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(EisensteinInt(1,0) + EisensteinInt(1,0), EisensteinInt(2,0))
        self.assertEqual(EisensteinInt(1,-1) + EisensteinInt(1,-1), EisensteinInt(2,-2))

    def test_mult(self):
        self.assertEqual(EisensteinInt(1,0) * EisensteinInt(1,0), EisensteinInt(1,0))
        self.assertEqual(EisensteinInt(10,0) * EisensteinInt(-1,0), EisensteinInt(-10,0))

    def test_sub(self):
        self.assertEqual(EisensteinInt(1,0) - EisensteinInt(1,0), EisensteinInt(0,0))
        self.assertEqual(EisensteinInt(1,-1) - EisensteinInt(1,-1), EisensteinInt(0,0))
        self.assertEqual(EisensteinInt(10,-1) - EisensteinInt(1,12), EisensteinInt(9,-13))
        self.assertEqual(EisensteinInt(5,-1) - EisensteinInt(10,-10), EisensteinInt(-5,9))

    def test_conjugate(self):
        self.assertEqual(EisensteinInt(0,1).conjugate(), EisensteinInt(-1,-1))
        self.assertEqual(EisensteinInt(1,0).conjugate(), EisensteinInt(1,0))

    def test_norm(self):
        # Norm of units are 1
        self.assertEqual(EisensteinInt(1,0).norm(), 1)
        self.assertEqual(EisensteinInt(-1,0).norm(), 1)
        self.assertEqual(EisensteinInt(0,1).norm(), 1)
        self.assertEqual(EisensteinInt(0,-1).norm(), 1)
        self.assertEqual(EisensteinInt(-1,-1).norm(), 1)
        self.assertEqual(EisensteinInt(1,1).norm(), 1)
        self.assertEqual(EisensteinInt(-2,-2).norm(), 4)
        self.assertEqual(EisensteinInt(1,-1).norm(), 3)

    def test_is_prime(self):
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
        units = EisensteinInt.units()
        self.assertEqual(EisensteinInt(1,0), units[0])
        self.assertEqual(EisensteinInt(-1,0), units[1])
        self.assertEqual(EisensteinInt(0,1), units[2])
        self.assertEqual(EisensteinInt(0,-1), units[3])
        self.assertEqual(EisensteinInt(-1,-1), units[4])
        self.assertEqual(EisensteinInt(1,1), units[5])

    def test_is_even(self):
        # Even iff. norm congruent to 0 mod 3
        # Not even iff. norm congruent to 1 mod 3
        self.assertTrue(EisensteinInt(1,-1).is_even())
        self.assertTrue(EisensteinInt(1,-1).norm() % 3 == 0)

        self.assertFalse(EisensteinInt(5,2).is_even())
        self.assertTrue(EisensteinInt(5,2).norm() % 3 == 1)

        self.assertFalse(EisensteinInt(5,8).is_even())


    def test_floor_div(self):
        self.assertEqual(EisensteinInt(1,-1) // EisensteinInt(1,-1), EisensteinInt(1))
        self.assertEqual(EisensteinInt(10,0) // EisensteinInt(5,0), EisensteinInt(2,0))

    def test_div_mod(self):
        result = EisensteinInt(13,0) % EisensteinInt(5,0)
        self.assertEqual(result, EisensteinInt(3,0), msg=str(result))

    def test_gcd(self):
        a=EisensteinInt(12,0)
        b=EisensteinInt(6,0)
        self.assertEqual(a.gcd(b), EisensteinInt(6,0))

        a=EisensteinInt(20,0)
        b=EisensteinInt(12,0)
        self.assertEqual(a.gcd(b), EisensteinInt(4,0))

if (__name__ == '__main__'):
    unittest.main()
