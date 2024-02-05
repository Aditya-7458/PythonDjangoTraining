def outer():
    x="local"
    def inner():
        nonlocal x
        x="nonlocal"
        print(x)
    inner()
    print(x)
outer()




#######33

def outer():
    x="local"
    def inner():
       # nonlocal x
        x="nonlocal"
        print(x)
    inner()
    print(x)
outer()


######

def fun1():
    x=20
    def fun2():
        global x
        x=25
    print(x)
    fun2()
    print(x)

fun1()
print(x)
