'''
# Explains Global and Local
x = "global"


def test():
    x = "local"
    print(x)


test()
print(x)'''
# runs global and then local

'''
# Explains Enclosing Scope
x = "global"


def outer():
    x = "outer"

    def inner():
        print(x)
        

    inner()


outer()'''

# Explains all of LEGB
'''x = "global"


def outer():
    #x = "enclosing"

    def inner():
        #x = "local"
        print(x)

    inner()


outer()'''

'''len = "hello"

def test():
    print(len([1, 2, 3]))

test()'''

'''x = 10

def test():
    global x
    x = 20

test()

print(x)'''

x = "global"

def outer():
    x = 20

    def inner():
        x = 30
        #print(x)

    inner()

outer()



