from eisenstein import EisensteinInt

a = EisensteinInt(-2,-2)
a.plot_point()
a.plot_multiples(n=1)

a = EisensteinInt(-2,5)
a.plot_point()
a.plot_multiples(n=2)

a = EisensteinInt(1,-2)
a.plot_point()
a.plot_multiples(n=3)

a = EisensteinInt(1,0)
a.plot_point()
a.plot_multiples(n=10, labels=False)

a = EisensteinInt(2,19)
a.plot_point()
a.plot_multiples(n=15, labels=False)
