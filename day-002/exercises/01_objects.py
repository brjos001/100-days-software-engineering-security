'''x = 42
# x is referring to the number 42

y = "hello"  
# y is referring to the string hello

z = []
# z is referring to the list 

print(type(x))
print(type(y))
print(type(z))

print(id(x))
print(id(y))'''

'''x = 42
y = 42

print(x is y)
print(x == y)'''

'''x = []
y = []

print(x is y)
print(x == y)'''

'''x = []
y = x

x.append("hello")

print(x)
print(y)
print(x is y)'''

'''y = [1]
y = x

y = [2]

print(x)
print(y)
print(x is y)'''

'''x = [1]
y = x

y.append(2)

x = 3 

print(x)
print(y)'''

# Mutation
# x.append(2)
# Chaning the existing object

# Reassignment
# x = [2]
# Make x refer to a different object

# x = []. Creates a list object
# y = x  Creates another reference to the same object
# x.append(1).  Mutates the existing object
# x = [2]. Creates a new obeject and rebinds x 