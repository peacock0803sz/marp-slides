# PyCon APAC 2021 CfP

## Talk title: Getting Started with Statically Typed Python in 2021

## Format: Talk(30-45 min)

## Audience Level: All

## Elevator Pitch

Now, Python is possible to write like the "typing" module statically typed.
By that, you can significantly enhance the development experience.
I'll start the talk with the basics of static-typing programming step-by-step.
It's included updates up to just released 3.10, writing knowledge, and best practices.

## Description

## Goals of this talk

- Basic usage of type hint
- What's new in 3.10's typing modules
- Best practice for developing with type hint

## Detail

I'll talk about static-typing programming in Python with the "typing" standard module.
In 2015, it appeared in Python 3.5, but it has only become common in the last few years.
However, over the years, there have been several big PEPs adopted and updated.
Even now, I think many people **don't know where to start** because there is little coherent information.

I'll also talk about this:

- Improving developing experiences throw taking advantage of the typing inference engine
- Perspectives on code reviews.
 
I have been

- Used type hints for almost two years in production
- Learned Haskell and typescript

Let me introduce the audiences to type hints based on those experiences.

## Timeline overview

1. Self-introduction, Overview of this session (5 min)
2. Introduction of typing, How to write basically (10 min)
3. Step-up: Advanced types (5 min)
4. Updates overview on 3.10, backword compatibility for 3.8 and 3.9 (10 min)
5. Design and develop with typing (10 min)
6. Conclusion & QA (5 min)
 
## Technical Requirements for audience

- Basic knowledge of Python 3.x grammar
- Experiences developing in statically typed language
    - Optional, not required

## Not talk about

- Developing library with typing
- Configures and options of mypy
- How to use them in CI
    - GitHub actions
    - Circle CI
- History of type hinting
- Detail of PEPs
- Implementation of typing, mypy
- Abstract Syntax Tree (AST)
 
## Detail of the Timeline plan

1. Self-introduction, Overview of this session (5 min)
2. Introduction of typing, How to write basically (10 min)
    1. Arguments and return value of functions
    2. Built-in types you can use without "import"
3. Step-up: Advanced types (5 min)
    1. Collections, Any
    2. Callable, TypeVar, Generic, etc
4. Updates overview on 3.10, backword compatibility for 3.8 and 3.9 (10 min)
    1. Update: Union operator `|`
    2. Update: Parameter Specification Variables (outline only)
    3. Update: Type aliases more explicitly (outline only).
    4. Backwards compatibility:`from __future__ import annotations`
5. Design and develop with typing (10 min)
    1. Support by Language Server and mypy
    2. Type-driven development
    3. Points of reviewing code
6. Conclusion & QA (5 min)

