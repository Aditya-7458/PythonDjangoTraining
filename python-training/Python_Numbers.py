# Python_Numbers
#Decimal 
from decimal import Decimal as d
a=0.3
b= 4.1
c= 0.3+4.1

print(c)
x=d('0.3') + d('4.1') # without this output will be 4.399999999999
print(x)


#Fractions

from fractions import Fraction as F
print(F(1.5))
print(F(5))
print(F(1,5))

# math modules 
import math as m
print(m.factorial(5))
print(m.pi)
print(m.exp(10))
print(int(abs(-12.34)))
print(abs(-12.34))

# Random 

import random as r
print(r.randrange(5,15))
print(r.randrange(5,15))
print(r.randrange(5,20))
print(r.randrange(1))

list=["Mon","Tue","Wed","Thru","Fri","Sat"]
print(r.choice(list))


r.shuffle(list)

print(list)

print(r.random())
