def maximum(a,b):    # function with parameter
    if a> b:
        return a
    else:
        return b
print(maximum(10,20))
print(maximum(200,10))



def hello(name,msg=",How are you"):  ## Function with default parameter
    print("Hello",name,msg)

hello("Aditya")
hello("Aditya","Good bye")



def add(*args): #Arbitory parameter , we can pass multiple number of argument in it
    sum=0
    for i in args:
        sum+=i
    return sum 
print(add(1,2,3,4))