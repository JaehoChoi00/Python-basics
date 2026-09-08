from Expresso import Expresso
from Enums import ExposureCategory, ExposureLevel


print("\n=== DEFAULT ===")

Expresso.printf(ExposureCategory.VANILLA, ExposureLevel.LEVEL1, "VANILLA L1\n")
Expresso.printf(ExposureCategory.DEBUG, ExposureLevel.LEVEL1, "DEBUG L1\n")
Expresso.printf(ExposureCategory.BITWISE, ExposureLevel.LEVEL1, "BITWISE L1\n")
Expresso.printf(ExposureCategory.TEST, ExposureLevel.LEVEL2, "TEST L2\n")


print("\n=== LEVEL 2 ===")

Expresso.setLevel(ExposureLevel.LEVEL2)

Expresso.printf(ExposureCategory.VANILLA, ExposureLevel.LEVEL1, "VANILLA L1\n")
Expresso.printf(ExposureCategory.DEBUG, ExposureLevel.LEVEL2, "DEBUG L2\n")
Expresso.printf(ExposureCategory.BITWISE, ExposureLevel.LEVEL3, "BITWISE L3\n")


print("\n=== SELECTED LEVELS ===")

Expresso.setLevels(ExposureLevel.LEVEL1, ExposureLevel.LEVEL3, ExposureLevel.LEVEL5)

Expresso.printf(ExposureCategory.DEBUG, ExposureLevel.LEVEL1, "DEBUG L1\n")
Expresso.printf(ExposureCategory.DEBUG, ExposureLevel.LEVEL2, "DEBUG L2\n")
Expresso.printf(ExposureCategory.DEBUG, ExposureLevel.LEVEL3, "DEBUG L3\n")
Expresso.printf(ExposureCategory.DEBUG, ExposureLevel.LEVEL4, "DEBUG L4\n")
Expresso.printf(ExposureCategory.DEBUG, ExposureLevel.LEVEL5, "DEBUG L5\n")


print("\n=== CATEGORY FILTER ===")

Expresso.setLevel(ExposureLevel.LEVEL5)
Expresso.setCategory(ExposureCategory.DEBUG)

Expresso.printf(ExposureCategory.DEBUG, ExposureLevel.LEVEL1, "DEBUG\n")
Expresso.printf(ExposureCategory.BITWISE, ExposureLevel.LEVEL1, "BITWISE\n")
Expresso.printf(ExposureCategory.TEST, ExposureLevel.LEVEL1, "TEST\n")


print("\n=== MULTIPLE CATEGORIES ===")

Expresso.setCategories(ExposureCategory.DEBUG, ExposureCategory.BITWISE)

Expresso.printf(ExposureCategory.DEBUG, ExposureLevel.LEVEL1, "DEBUG\n")
Expresso.printf(ExposureCategory.BITWISE, ExposureLevel.LEVEL1, "BITWISE\n")
Expresso.printf(ExposureCategory.TEST, ExposureLevel.LEVEL1, "TEST\n")


print("\n=== CLEAR CATEGORY FILTER ===")

Expresso.clearAllCategories()

Expresso.printf(ExposureCategory.DEBUG, ExposureLevel.LEVEL1, "DEBUG\n")
Expresso.printf(ExposureCategory.BITWISE, ExposureLevel.LEVEL1, "BITWISE\n")
Expresso.printf(ExposureCategory.TEST, ExposureLevel.LEVEL1, "TEST\n")


print("\n=== IDENTITY ===")

exposure = Expresso.exposure("TestEngine")

exposure.l1(ExposureCategory.SYSTEMLOG, "Engine started\n")
exposure.l2(ExposureCategory.COMPONENTIAL, "Loading component: %s\n", "Renderer")
exposure.l3(ExposureCategory.LOWERLEVEL, "Internal value: %d\n", 42)


print("\n=== LAZY ===")

exposure.l1(ExposureCategory.DEBUG, lambda: "Lazy message\n")
exposure.l5(ExposureCategory.DEBUG, lambda: "Lazy deep message\n")


print("\n=== NEWLINE ===")

exposure.nl(ExposureCategory.DEBUG, ExposureLevel.LEVEL1)
exposure.lbr(ExposureCategory.DEBUG, ExposureLevel.LEVEL1)


print("\n=== ERROR ===")

exposure.err("Something went wrong: %s\n", "test")

try:
    1 / 0
except Exception as exception:
    exposure.err("Division failed\n", exception)


print("\n=== HERE ===")

exposure.here()
exposure.here("Reached renderer initialization")


print("\n=== TAGS ===")

Expresso.enableTimestamp(True)
Expresso.enableElapsedTime(True)

exposure.l1(ExposureCategory.SYSTEMLOG, "Timestamp and elapsed time\n")


print("\n=== INDEX ===")

Expresso.resetEventCounter()

exposure.l1(ExposureCategory.DEBUG, "Event 1\n")
exposure.l1(ExposureCategory.DEBUG, "Event 2\n")
exposure.l1(ExposureCategory.DEBUG, "Event 3\n")

print("Current event count:", Expresso.getCurrentEventCount())


print("\n=== INDEX FILTER ===")

Expresso.setSingleIndex(5)

exposure.l1(ExposureCategory.DEBUG, "Event 4\n")
exposure.l1(ExposureCategory.DEBUG, "Event 5\n")
exposure.l1(ExposureCategory.DEBUG, "Event 6\n")


print("\n=== RESET ===")

Expresso.clearIndexFilter()
Expresso.clearAllCategories()
Expresso.setLevel(ExposureLevel.LEVEL1)
Expresso.enableTimestamp(False)
Expresso.enableElapsedTime(False)

print("Categories:", Expresso.getCategories())
print("Levels:", Expresso.getLevels())
print("Event count:", Expresso.getCurrentEventCount())