from eisenstein import EisensteinInt

a=EisensteinInt(3,1) # 3 + w
b=EisensteinInt(2, -1) # 3 + w**2
r1=EisensteinInt(1,0)
d=(a*b)+r1
q,r2 = divmod(d, a)

print(q, b)
print(r1, r2)

print("*********")

d=(a*b)+r1
q,r2 = d.divmod_test(a)

print(q, b)
print(r1, r2)
# for x in (a.gcd(b).associates()):
#     if p == x:
#         print("gcd in associates")
#     print(x)
#
# print("P", p)
