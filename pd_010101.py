# add and multiply two complex numbers of the form a(n) + b(n) * i

a1 = float(input("a1 = "))
b1 = float(input("b1 = "))
a2 = float(input("a2 = "))
b2 = float(input("b2 = "))

c1 = str(a1) + " + " + str(b1) + " * i"
c2 = str(a2) + " + " + str(b2) + " * i"

r1 = str(a1 + a2)
i1 = str(b1 + b2)

r2 = str(a1 * a2 - b1 * b2)
i2 = str(a1 * b2 + b1 * a2)

print("(", c1, ") + (", c2, ") = (", r1, "+", i1, "* i )", sep=" ")
print("(", c1, ") + (", c2, ") = (", r2, "+", i2, "* i )", sep=" ")
