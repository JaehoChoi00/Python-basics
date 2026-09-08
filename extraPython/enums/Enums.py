from enum import Enum, auto, Flag

class EnumClass(Enum):
    ENUMVARIABLE1 = 1
    ENUMVARIABLE2 = 2
    ENUMVARIABLE3 = 3
    NEXTVARIABLE4 = auto()

print(EnumClass.ENUMVARIABLE1.name + " = " + str(EnumClass.ENUMVARIABLE1.value))
print(EnumClass.ENUMVARIABLE2.name + " = " + str(EnumClass.ENUMVARIABLE2.value))
print(EnumClass.ENUMVARIABLE3.name + " = " + str(EnumClass.ENUMVARIABLE3.value))
print(EnumClass.NEXTVARIABLE4.name + " = " + str(EnumClass.NEXTVARIABLE4.value))

class BinaryFlag(Flag):
    BINARY1 = auto()       # 1  (0001)
    BINARY2 = auto()      # 2  (0010)
    BINARY3 = auto()    # 4  (0100)
    BINARY4 = auto()     # 8  (1000)

print(BinaryFlag.BINARY1.name + " = " + str(BinaryFlag.BINARY1.value))
print(BinaryFlag.BINARY2.name + " = " + str(BinaryFlag.BINARY2.value))
print(BinaryFlag.BINARY3.name + " = " + str(BinaryFlag.BINARY3.value))
print(BinaryFlag.BINARY4.name + " = " + str(BinaryFlag.BINARY4.value))