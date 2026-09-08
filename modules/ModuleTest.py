import Modules

print(dir(Modules))

print(Modules.moduleFunction())
print(Modules.moduleVariable)
print("Module Variable 1: " + Modules.moduleVariable)
print("Module Variable 2: " + str(Modules.moduleVariable2))
print("Module Variable 3: " + str(Modules.moduleVariable3))
print("Variable 2 + Variable 3 = " + str(Modules.moduleVariable2 + Modules.moduleVariable3))
print("_SpecialVariable: " + Modules._SpecialVariable)
print()

from Modules import *

print(moduleFunction())
print(moduleVariable)
print("Module Variable 1: " + moduleVariable)
print("Module Variable 2: " + str(moduleVariable2))
print("Module Variable 3: " + str(moduleVariable3))
print("Variable 2 + Variable 3 = " + str(moduleVariable2 + moduleVariable3))
print("_SpecialVariable cannot be seen")
print()

import Modules as customModuleName

print(moduleFunction())
print(customModuleName.moduleVariable)
print("Module Variable 1: " + customModuleName.moduleVariable)
print("Module Variable 2: " + str(customModuleName.moduleVariable2))
print("Module Variable 3: " + str(customModuleName.moduleVariable3))
print("Variable 2 + Variable 3 = " + str(customModuleName.moduleVariable2 + customModuleName.moduleVariable3))
print("_SpecialVariable: " + customModuleName._SpecialVariable)
print()

moduleVariable2 = 5
print("It will still print the original: " + str(Modules.moduleVariable2))
