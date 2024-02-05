# Defining a closure function

def print_msg(msg):
    def print_msg_inner():
        print(msg)
    return print_msg_inner

new=print_msg("Hello")
new()



# Function as object
def outer():
    print("Hiiii")

print(outer)

print(type(outer))


# nested function

def outer1():
    def inner1():
        print("heeeeello")
    inner1()

outer1()

# aliasing function

def outer2():
    def inner2():
        a=10;b=23
        sum=a+b
        return sum
    return inner2
    
inner2=outer2()
print(inner2())






