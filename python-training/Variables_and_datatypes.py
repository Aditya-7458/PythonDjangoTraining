 # Variables - It is lke a container which store data like number , name , decimal number etc.

a= 1  
b= True
c= "Aditya"
d= None 
print(a)
print(b)
print(c)
print(d)

'''
Data Type 

1. Numeric data

   int  - 3,-4,0
   float - 6.888,0.00001
   complex - 6 + 2i

2. Text data
   a="Hello world "

3. Boolean data 
   a= True
   b= False 

4. Sequenced data
   list
   Tupple
5. Mapped data 
   dict

'''

zz= 10.01
print(zz)

num=10000000000000000000000000000 # no need to worry about range to variable 
suum=num+34
print(suum)
print(type(suum))
print(type(zz))


'''
Scope of variable 
1. Global - Variables defined outside any function or block have a global scope. They are accessible throughout the entire program.
2. Local - Variables defined inside a function have a local scope. They are only accessible within that function.

'''

# Local scope
def f1():
    var= 10
    print(var)

f1() 
#  print(var) it show error 




# Global scope
varr= 20

def f2():
    print(varr)

f2()

