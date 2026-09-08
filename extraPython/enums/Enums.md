# Enums

[:arrow_left: Return to Main README](../../README.md)

> This is a full rundown of the [`Enums.py`](/extraPython/enums/Enums.py) file

> ---

> **Terminal code for running**:
> ```bash
> python3 Enums.py
> ```

## Sections:

> * [`EnumClass`](#enumclass)
> * [`BinaryFlag`](#binaryflag)
> * [`Testing`](#testing)

---

### [EnumClass](#sections)

********Python Syntax********

```py
from enum import Enum, auto

class EnumClass(Enum):

    ENUMVARIABLE1 = 1

    ENUMVARIABLE2 = 2

    ENUMVARIABLE3 = 3

    NEXTVARIABLE4 = auto()
```

### [BinaryFlag](#sections)

********Python Syntax********

```py
from enum import Flag, auto

class BinaryFlag(Flag):

    BINARY1 = auto()       # 1  (0001)

    BINARY2 = auto()       # 2  (0010)

    BINARY3 = auto()       # 4  (0100)

    BINARY4 = auto()       # 8  (1000)
```

### [Testing](#sections)

***Python Syntax***

```py
print(EnumClass.ENUMVARIABLE1.name + " = " + str(EnumClass.ENUMVARIABLE1.value))

print(EnumClass.ENUMVARIABLE2.name + " = " + str(EnumClass.ENUMVARIABLE2.value))

print(EnumClass.ENUMVARIABLE3.name + " = " + str(EnumClass.ENUMVARIABLE3.value))

print(EnumClass.NEXTVARIABLE4.name + " = " + str(EnumClass.NEXTVARIABLE4.value))

print(BinaryFlag.BINARY1.name + " = " + str(BinaryFlag.BINARY1.value))

print(BinaryFlag.BINARY2.name + " = " + str(BinaryFlag.BINARY2.value))

print(BinaryFlag.BINARY3.name + " = " + str(BinaryFlag.BINARY3.value))

print(BinaryFlag.BINARY4.name + " = " + str(BinaryFlag.BINARY4.value))
```

***Output***

```txt
ENUMVARIABLE1 = 1
ENUMVARIABLE2 = 2
ENUMVARIABLE3 = 3
NEXTVARIABLE4 = 4
BINARY1 = 1
BINARY2 = 2
BINARY3 = 4
BINARY4 = 8
```
