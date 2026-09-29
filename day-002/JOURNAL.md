Day 2 Journal — Objects, Names & References
What I Learned

Python names refer to objects. A name is not the object itself.

For example:

x = 42


can be thought of as:

x ──→ 42


The name x refers to the integer object 42.

Multiple Names Can Refer to One Object
x = 42
y = x


Both x and y refer to the same object.

x ──┐
    ↓
   42
    ↑
y ──┘


The fact that there are two names does not mean there are two objects.

Mutation

Lists are mutable.

x = []
y = x

x.append("hello")


Both x and y see the change because they refer to the same list object.

x ──┐
    ↓
["hello"]
    ↑
y ──┘

Rebinding

Rebinding is different from mutation.

x = [1]
y = x

x = [2]


The second assignment creates a new list and makes x refer to it.

The original list is still referenced by y.

x ──→ [2]

y ──→ [1]

Identity vs Equality

I learned the basic distinction:

x is y


asks whether two names refer to the same object.

x == y


asks whether the objects compare as equal.

Two separate lists can have equal contents without being the same object:

x = []
y = []

x is y    # False
x == y    # True

My Main Takeaway

The most important idea from Day 2 is:

Names refer to objects.

When analyzing Python code, I should ask:

What objects exist?

What names exist?

Which names refer to each object?

Did an operation mutate an existing object?

Did an assignment rebind a name to a new object?

Mistake I Made

I initially thought that different names might automatically mean different objects.

The exercises showed that:

x = 42
y = x


can have two names referring to the same object.

I also initially treated reassignment and mutation as similar operations. They are not.

Day 2 Conclusion

I can now distinguish between:

an object

a name

a reference

mutation

rebinding

identity

equality

This gives me a foundation for understanding more complicated Python state and data flow.
