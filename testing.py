from eisenstein import EisensteinInt


a=EisensteinInt(17,0)
b=EisensteinInt(9,0)
# self.assertEqual(a // b , EisensteinInt(-2,0))

# a=EisensteinInt(8,0)
# b=EisensteinInt(3,1)
# a=EisensteinInt(3,21)
# b=EisensteinInt(-34, -1)
# r1=EisensteinInt(1,0)
# d=(a*b)+r1

q,r2 = divmod(a,b)
print(q,"\t", r2)
# a=EisensteinInt(17,0)
# b=EisensteinInt(9,0)
# c=EisensteinInt(1,0)
# r1=EisensteinInt(8,0)
# q,r2 = divmod(a, b)
#
# print("Quotient - Expected:", c, "\tActual:", q)
# print("Remainder - Expected:", r1, "\tActual:", r2)
#
# a=EisensteinInt(3,21)
# b=EisensteinInt(-34, -1)
# r1=EisensteinInt(1,0)
# d=(a*b)+r1
#
# q,r2 = divmod(d, a)
#
# print("A: ", a, "\tB: ", b, "\tA//B: ",q)
#
# print("Quotient - Expected:", b, "\tActual:", q)
# print("Remainder - Expected:", r1, "\tActual:", r2)
#
# a=EisensteinInt(20,0)
# b=EisensteinInt(-10,0)
# c=EisensteinInt(-2,0)
# r1=EisensteinInt(0,0)
# q,r2 = divmod(a, b)
#
# print("Quotient - Expected:", c, "\tActual:", q)
# print("Remainder - Expected:", r1, "\tActual:", r2)


# a=EisensteinInt(-3,21)
# b=EisensteinInt(5, -1)
# r1=EisensteinInt(1,0)
# d=(a*b)+r1
#
# q,r2 = divmod(d, a)
# self.assertTrue(r1 == r2)
# self.assertTrue(q == b)
# b=EisensteinInt(5,2)
# c= a*b
# r = EisensteinInt(0, 2)
# c= c +r
# a=EisensteinInt(3,2)
# b=EisensteinInt(5,2)
# c= a*b
# r = EisensteinInt(0, 2)
# c= c +r
# print(divmod(a,b)[0])
