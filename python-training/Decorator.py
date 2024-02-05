
# using closures (Decorator)
def decor(func):
    def inner():
        func()
        print("Hello")
    return inner

def pp():
    print("hello")
    print("hello")

pp=decor(pp)
pp()


# using @ 
def decor(func):
    def inner():
        func()
        print("Hello")
    return inner
@decor
def pp():
    print("hello")
    print("hello")



# Addition 
    
def decor2(func):
    def inner():
      
        num3=int(input("Enter the third number"))
        result=func()+ num3
        return result
    return inner

    
@decor2
def add():
    num1=float(input("Enter first number"))
    num2=float(input("Enter second number"))
    result=num1+num2
    return result
print(add())



# Multiple decorator on one function




def decor3(func):
    def inner():
        result=func().upper()
        return result
    return inner 

def decor4(func):
    def inner():
        result=func().split()
        return result
    return inner




@decor4
@decor3
def get_name():
    name=input("Enter First Name")
    name2=input("Enter Second Name")
    return name+" "+name2
print(get_name())


# one decorator on multiple function
def decor5(func):
    def inner(*args):
        for num in args[1:]:
            if num==0:
                return ("Cannot devide by Zero")
        return func(*args)
    return inner 

@decor5
def div1(a,b):
    return a/b
@decor5
def div2(a,b,c):
    return a/b/c

print(div1(0,4))
print(div2(1,4,0))


# Smart divider using decorator
def smart_divider(func):
    def inner(num1,num2):
        if num1==0:
            print("Can not devide by zero ")
            return 
        func(num1,num2)
    return inner

@smart_divider
def div(num1,num2):
    print(num1/num2)

div(10,10)




