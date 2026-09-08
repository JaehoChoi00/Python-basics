# Lambda

[:arrow_left: Return to Main README](../../README.md)

> This is a full rundown of the [`Lambda.ipynb`](/extraPython/lambda/Lambda.ipynb) file

> ---
> 
## Sections:

> * [`Lambda Function`](#lambda-function)
> * [`Multiple Parameters`](#multiple-parameters)
> * [`Testing`](#testing)

---

### [Lambda Function](#sections)

***Python Syntax***

```py
def someExpression(parameter):

    print("The inputted variable " + str(parameter) + " of type " + str(type(parameter)))

    if isinstance(parameter, int):
        parameter += 10
        print("Adding 10 to the variable: " + str(parameter))

    elif isinstance(parameter, str):
        print("Title case all string: " + parameter.title())


lambdaFunction = lambda argument : someExpression(argument)
```

### [Multiple Parameters](#sections)

***Python Syntax***

```py
def someExpression(par1, par2, par3):
    print("The inputted parameter 1 [ " + str(par1) + " ] of type " + str(type(par1)))
    print("The inputted parameter 2 [ " + str(par2) + " ] of type " + str(type(par2)))
    print()

    if isinstance(par1, int) and isinstance(par2, int) and isinstance(par3, int):
        par1 += 10
        print("Adding 10 to the variable: " + str(par1))
        return par1

    elif isinstance(par1, str):
        print("Title case all string: " + par1.title())
        return par1.title()


lambdaFunction = lambda arg1, arg2, arg3 : someExpression(arg1, arg2, arg3)
```

### [Testing](#sections)

***Python Syntax***

```py
input = 5
lambdaFunction(5, 10, 15)
lambdaFunction("hello world", 2, 3)
lambdaFunction(input)
```

***Output***

```txt
The inputted parameter 1 [ 5 ] of type <class 'int'>
The inputted parameter 2 [ 10 ] of type <class 'int'>

Adding 10 to the variable: 15

The inputted parameter 1 [ hello world ] of type <class 'str'>
The inputted parameter 2 [ 2 ] of type <class 'int'>

Title case all string: Hello World
```

> `lambdaFunction(input)` raises a `TypeError` because the lambda requires three arguments.
