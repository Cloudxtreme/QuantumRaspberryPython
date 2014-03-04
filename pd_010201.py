# subtract and divide complex numbers. also return the modulus and conjugate
import math

a1 = float(input("a1 = "))
b1 = float(input("b1 = "))
a2 = float(input("a2 = "))
b2 = float(input("b2 = "))

c1 = str(a1) + " + " + str(b1) + " * i"
c2 = str(a2) + " + " + str(b2) + " * i"

r1 = str(a1 - a2)
i1 = str(b1 - b2)

md2 = a2 ** 2 + b2 ** 2
md = str(math.sqrt(md2))
r2 = str((a1 * a2 + b1 * b2) / md2)
i2 = str((a2 * b1 - a1 * b2) / md2)

print("(", c1, ") - (", c2, ") =", r1, "+", i1, "* i", sep=" ")
print("(", c1, ") / (", c2, ") =", r2, "+", i2, "* i", sep=" ")
print("modulus(", a2, "^ 2 +", b2, "^ 2 ) =", md, sep=" ")
print("conjugate(", a2, "+", b2, "* i ) =", a2, "-", b2, "* i", sep=" ")
