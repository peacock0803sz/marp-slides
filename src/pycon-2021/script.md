
---

Hi, let's start.

---

# Hello EuroPython!

Before the main content, let me to introduce myself.
If you have any questions or comments, please write here. I'd love to hear from you during the talk.

---

# Self-introduction

Nice to meet you...
In addition to my work, I'm also involved in the following activities

---

# Introducing and promotion from PyCon JP

Let me give you one more promotion about PyCon JP 2021

---

# PyCon JP 2020 was held in online!

PyCon JP 2020 was held online. The photo is from the toast of the party.

---

# :mega: Announces about PyCon JP 2021 (1/2)

there are Website, blog and twitter links.
The date of the conference is Oct. 15,16.
We haven't decided what we will do for sprints and training yet.
Now, CfP is over. We are currently in the process of review and adoption.

---

# :mega: Announces about PyCon JP 2021 (2/2)

The venue could be both online or hybrid.

---

# Today's topic

this is today's topic.
...

---

# Why I talk about typing?

My motivation for talking is to get the word out in a coherent way.
It's been five years (Python 3.5, at 2015) since typing appeared

---

# Inro of typing

OK, Let's take a look at how to actually start Typing!

---

# What makes you happy?

First, let's look at what typing can do for you.

In the editor, you can see what type you are trying to use.
You can see that the example uppper half is a function that receives str and returns str.
In the lower part, str is expected, but since we are passing an int, we get an error message.

---

# Built-in types

First, let's take a look at the simplest type.
...


---

# Using different types of collections


There are many types in `collections.abc.` 

Although it's unlikely that you will use these in a fine-grained way, It's better to choose a collection with as few  methods as possible to increase portability.

The following figure shows the relationship between `collections.abc` and a sequence of built-in types defined by method inclusion rather than implementation inheritance. 

The further to the left you go, the fewer methods it has, and the further to the right, the more methods it has. 

It is a good idea to look at the methods used in your functions and choose the types on the left side of this diagram as much as possible.

---

For example, if you just want to loop over a sequence of arguments in a function, you can use collections.abc.Iterable. Iterable. If you need random access, use Sequence. If you need to change the value, use a type with Mutable.

Or, if you simply specify list as the argument type, you will not be able to pass set or dict. In particular, it is better not to set concrete types (list, tuple, dictionary, set) just because you are familiar with them. However, I think it is easier to understand using these concrete types, so you may want to try applying these concrete types first, and after you confirm that you can use fewer operators and methods, you may want to gradually move to the left side of the types.

---

# any

It is strictly forbidden to abuse, but it can be used like this
it's very evil!!!

---

# A little more advanced: Generics type

Next, there are few advaced types.

---

# Union (Mager type)

at first is union, merged type.
top half code is an Example A function that accepts both integers and float
bottom one is Union objects can be tested for equality with other union objects.

---

# User-defined Generic types

A generic type is typically declared by inheriting from an instantiation of this class with one or more type variables.

---

...

---

# What is the `__future__` module: (dunder future)?
Let's talk about dunder future, which has come up many times before.
Modules and methods with two underscores at either end are pronounced dunder.

---

# New Features Related to Type Hints in 3.10
next topic is new features in python3.10, will be released Nov. this year
there're few very difficult features. I'm not sure I can explain it well either.

---

# Summary

