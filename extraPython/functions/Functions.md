# Functions

[:arrow_left: Return to Main README](../../README.md)

> This is a full rundown of the [`Functions.ipynb`](/extraPython/functions/Functions.ipynb) file

> ---

## Sections:

> * [`Basic Function`](#basic-function)
> * [`Function Parameters`](#function-parameters)
> * [`Multiple Parameters`](#multiple-parameters)
> * [`Variable Length Arguments`](#variable-length-arguments)

---

### [Basic Function](#sections)

***Python Syntax***

```py
def thisIsAFunction():

    print("I am a function")

thisIsAFunction()
```

***Output***

```txt
I am a function
```

### [Function Parameters](#sections)

***Python Syntax***

```py
def functionWithParameter(parameter):

    print("parameter: " + str(parameter))

functionWithParameter("This is a parameter")
```

***Output***

```txt
parameter: This is a parameter
```

### [Multiple Parameters](#sections)

***Python Syntax***

```py
def functionWithTwoParameter(parameter1, parameter2):

    print("Inputted parameter1: " + str(parameter1))

    print("Inputted parameter2: " + str(parameter2))

    print()

    if (isinstance(parameter1, int) and isinstance(parameter2, int)):

        print("parameter 1 and 2 is an int: adding together = " + str(parameter1 + parameter2))

functionWithTwoParameter("This is parameter 1", "This is parameter 2")

functionWithTwoParameter(1, 2)
```

***Output***

```txt
Inputted parameter1: This is parameter 1
Inputted parameter2: This is parameter 2

Inputted parameter1: 1
Inputted parameter2: 2

parameter 1 and 2 is an int: adding together = 3
```

### [Variable Length Arguments](#sections)

***Python Syntax***

```py
def functionWithVariableLengthArg(*args):

    print(args)

    print()

    for items in args:

        print(items)

functionWithVariableLengthArg(1, 2, 3, 4, 5, "Hello there", True)
```

***Output***

```txt
(1, 2, 3, 4, 5, 'Hello there', True)

1
2
3
4
5
Hello there
True
```
