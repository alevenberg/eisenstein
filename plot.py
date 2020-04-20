from eisenstein import EisensteinInt

a = EisensteinInt(-2,-2)
a.plot_point(file_name="./plots/1")
a.plot_multiples(n=1, file_name="./plots/1-1")

a = EisensteinInt(-2,5)
a.plot_point(file_name="./plots/2")
a.plot_multiples(n=2, file_name="./plots/2-1")

a = EisensteinInt(1,-2)
a.plot_point(file_name="./plots/3")
a.plot_multiples(n=3, file_name="./plots/3-1")

a = EisensteinInt(1,0)
a.plot_point(file_name="./plots/4")
a.plot_multiples(n=10, labels=False, file_name="./plots/4-1")

a = EisensteinInt(2,19)
a.plot_point(file_name="./plots/5")
a.plot_multiples(n=15, labels=False, file_name="./plots/5-1")

EisensteinInt.plot_all(n=1, primes=True, file_name="./plots/6-1")
EisensteinInt.plot_all(n=2,primes=True, file_name="./plots/6-2")
EisensteinInt.plot_all(n=3,primes=True, file_name="./plots/6-3")
EisensteinInt.plot_all(n=4, primes=True, file_name="./plots/6-4")
