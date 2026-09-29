Day 2 — Objects, Names & References
Goal

Build a correct mental model of how Python names, objects, and references work.

The goal is not simply to memorize Python behavior. The goal is to be able to look at code and reason about:

What objects exist?

What names exist?

Which names refer to which objects?

When is a new object created?

When is an existing object mutated?

When is a name rebound to a different object?

Concepts

Objects

Names

References

Assignment and rebinding

Mutation

Object identity

id()

is

==

Mutable vs immutable objects

Core Mental Model

Python names refer to objects.

For example:

x = []
y = x


creates one list object and two names referring to it:

x ──┐
    ↓
   []
    ↑
y ──┘


Mutating the object through one reference is visible through the other:

x.append(1)


Rebinding a name is different:

x = [2]


This makes x refer to a new object. It does not change the object that y refers to.

Key Distinction

Mutation:

x.append(2)


changes an existing object.

Rebinding:

x = [2]


makes x refer to a different object.

Day 2 Principle

Think in terms of an object graph rather than thinking that variables "contain" values.
