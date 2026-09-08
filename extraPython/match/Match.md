# Conditionals

[:arrow_left: Return to Main README](../../README.md)

> This is a full rundown of the [`Conditionals.ipynb`](/extraPython/match/Match.ipynb) file

> ---

**## Sections:**

> * [`If Statement`](#if-statement)
> * [`Match Statement`](#match-statement)
> * [`Testing`](#testing)

---

### [If Statement](#sections)

***Python Syntax***

```py
firstNumber = 0
secondNumber = 2

if firstNumber < secondNumber:
    print(firstNumber < secondNumber)
```

### [Match Statement](#sections)

***Python Syntax***

```py
keyPressedCoordinate = 5
match (keyPressedCoordinate):
    case 0:
        print("Numkey 0")
    case 1:
        print("Numkey 1")
    case 2:
        print("Numkey 2")
    case 3:
        print("Numkey 3")
    case 4:
        print("Numkey 4")
    case 5:
        print("Numkey 5")
    case 6:
        print("Numkey 6")
    case 7:
        print("Numkey 7")
    case 8:
        print("Numkey 8")
    case 9:
        print("Numkey 9")
```

### [Testing](#sections)

***Python Syntax***

```py
firstNumber = 0
secondNumber = 2

if firstNumber < secondNumber:
    print(firstNumber < secondNumber)

keyPressedCoordinate = 5

match (keyPressedCoordinate):
    case 0:
        print("Numkey 0")
    case 1:
        print("Numkey 1")
    case 2:
        print("Numkey 2")
    case 3:
        print("Numkey 3")
    case 4:
        print("Numkey 4")
    case 5:
        print("Numkey 5")
    case 6:
        print("Numkey 6")
    case 7:
        print("Numkey 7")
    case 8:
        print("Numkey 8")
    case 9:
        print("Numkey 9")
```

***Output***

```txt
True
Numkey 5
```
