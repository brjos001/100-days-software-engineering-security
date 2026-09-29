Day 2 Roadmap — Objects, Names & References
Objectives

 Understand what an object is

 Understand names/references

 Understand that multiple names can refer to one object

 Understand assignment/rebinding

 Understand mutation

 Distinguish identity from equality

 Understand the basic purpose of is

 Understand the basic purpose of id()

 Practice reasoning about object graphs

Exercises
Exercise 1 — Objects

Create objects and inspect their types.

Exercise 2 — Shared References
x = 42
y = x


Reason about how many objects and names exist.

Exercise 3 — Mutable Objects
x = []
y = x

x.append("hello")


Observe how mutation affects both references.

Exercise 4 — Rebinding
x = [1]
y = x

x = [2]


Observe the difference between mutation and rebinding.

Exercise 5 — Combined State
x = [1]
y = x

y.append(2)

x = [3]


Determine the final objects and references without running the code first.

Final Mental Model

Always ask:

What objects exist?

What names exist?

Which names point to which objects?

Did this operation mutate an object?

Or did it rebind a name?

Next Day

Day 3 — Identity, Equality & id()
