from eisenstein import EisensteinInt

a=EisensteinInt(3,1) # 3 + w
b=EisensteinInt(2, -1) # 3 + w**2
r1=EisensteinInt(1,0)
d=(a*b)+r1
q,r2 = divmod(d, a)

print("got:", q, "\texpected:", b)
print("got:", r1, "\texpected:", r2)

print("*********")

d=(a*b)+r1
q,r2 = d.divmod_brute_force(a)

print("got:", q, "\texpected:", b)
print("got:", r1, "\texpected:", r2)
