x = [1]
y = x

y.append(2)

x = [3]

print(x)
print(y)
print(x is y)

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