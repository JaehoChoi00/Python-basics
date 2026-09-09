import sys
import time
import traceback
from datetime import datetime
from enum import Enum
from threading import Lock

from Enums import ExposureCategory, ExposureLevel, ExposureTimeSource
import VariableConstants


class Expresso:

    globalEventCounter = 0
    counterLock = Lock()

    minIndex = 0
    maxIndex = float("inf")

    showIndexTag = True
    showIdentityTag = True
    showCategoryTag = True
    showLevelTag = True

    timeSource = None
    showApplicationTimeTag = False
    showTimestampTag = False
    showElapsedTimeTag = False

    DEFAULT_ERROR_PREFIX = "[ERROR]: "
    DEFAULT_ERROR_COLOR = VariableConstants.BOLD + VariableConstants.FG_RED

    DEFAULT_HERE_HEADER = "--> [EXPRESSO REPORT HERE]"
    DEFAULT_HERE_COLOR = VariableConstants.BOLD + VariableConstants.FG_MAGENTA

    errorPrefix = DEFAULT_ERROR_PREFIX
    errorColor = DEFAULT_ERROR_COLOR

    hereHeader = DEFAULT_HERE_HEADER
    hereColor = DEFAULT_HERE_COLOR

    showDiagnosticTags = False

    enabledCategories = set()

    enabledLevels = { ExposureLevel.LEVEL1 }
    levelsLock = Lock()

    externalBridge = None

    runtimeStart = time.perf_counter()

    RESET = VariableConstants.RESET
    BOLD = VariableConstants.BOLD
    DIM = VariableConstants.DIM
    UNDERLINE = VariableConstants.UNDERLINE
    LINEFEED = VariableConstants.LINEFEED

    FG_BLACK = VariableConstants.FG_BLACK
    FG_RED = VariableConstants.FG_RED
    FG_GREEN = VariableConstants.FG_GREEN
    FG_YELLOW = VariableConstants.FG_YELLOW
    FG_BLUE = VariableConstants.FG_BLUE
    FG_MAGENTA = VariableConstants.FG_MAGENTA
    FG_CYAN = VariableConstants.FG_CYAN
    FG_WHITE = VariableConstants.FG_WHITE

    BG_BLACK = VariableConstants.BG_BLACK
    BG_RED = VariableConstants.BG_RED
    BG_GREEN = VariableConstants.BG_GREEN
    BG_YELLOW = VariableConstants.BG_YELLOW
    BG_BLUE = VariableConstants.BG_BLUE
    BG_MAGENTA = VariableConstants.BG_MAGENTA
    BG_CYAN = VariableConstants.BG_CYAN
    BG_WHITE = VariableConstants.BG_WHITE

    @staticmethod
    def FG_COLOR(id): return VariableConstants.FG_COLOR(id)

    @staticmethod
    def BG_COLOR(id): return VariableConstants.BG_COLOR(id)

    @staticmethod
    def exposure(identity = None): return Exposure(identity)

    @staticmethod
    def enableIndexTag(enable): Expresso.showIndexTag = enable

    @staticmethod
    def enableIdentityTag(enable): Expresso.showIdentityTag = enable

    @staticmethod
    def enableCategoryTag(enable): Expresso.showCategoryTag = enable

    @staticmethod
    def enableLevelTag(enable): Expresso.showLevelTag = enable

    @staticmethod
    def enableTimestamp(enable): Expresso.showTimestampTag = enable

    @staticmethod
    def enableElapsedTime(enable): Expresso.showElapsedTimeTag = enable

    @staticmethod
    def setIndexRange(start, end = None):
        if end is None:
            Expresso.minIndex = 0
            Expresso.maxIndex = start
        else:
            Expresso.minIndex = max(0, start)
            Expresso.maxIndex = max(start, end)

    @staticmethod
    def setSingleIndex(targetIndex): Expresso.setIndexRange(targetIndex, targetIndex)

    @staticmethod
    def setErrorStyle(color = None, prefix = None):
        if color is not None: Expresso.errorColor = color
        if prefix is not None: Expresso.errorPrefix = prefix

    @staticmethod
    def setHereStyle(color = None, header = None):
        if color is not None: Expresso.hereColor = color
        if header is not None: Expresso.hereHeader = header

    @staticmethod
    def resetErrorStyle():
        Expresso.errorColor = Expresso.DEFAULT_ERROR_COLOR
        Expresso.errorPrefix = Expresso.DEFAULT_ERROR_PREFIX

    @staticmethod
    def resetHereStyle():
        Expresso.hereColor = Expresso.DEFAULT_HERE_COLOR
        Expresso.hereHeader = Expresso.DEFAULT_HERE_HEADER

    @staticmethod
    def enableDiagnosticTags(enable): Expresso.showDiagnosticTags = enable

    @staticmethod
    def clearIndexFilter():
        Expresso.minIndex = 0
        Expresso.maxIndex = float("inf")

    @staticmethod
    def resetEventCounter():
        with Expresso.counterLock: Expresso.globalEventCounter = 0

    @staticmethod
    def clearAllCategories(): Expresso.enabledCategories = set()

    @staticmethod
    def enableCategory(category):
        if category is not None: Expresso.enabledCategories.add(category.name)

    @staticmethod
    def disableCategory(category):
        if category is not None: Expresso.enabledCategories.discard(category.name)

    @staticmethod
    def NEWLINE(category, requiredLevel):
        if Expresso.isExposed(category, requiredLevel): Expresso.emit("\n\n")

    @staticmethod
    def LINEBREAK(category, requiredLevel):
        if Expresso.isExposed(category, requiredLevel): Expresso.emit("\n--------------------------------\n")

    @staticmethod
    def setLevel(newLevel):
        with Expresso.levelsLock:
            Expresso.enabledLevels.clear()
            if newLevel is not None: Expresso.enabledLevels.add(newLevel)

    @staticmethod
    def setLevels(*handPickedLevels):
        with Expresso.levelsLock:
            Expresso.enabledLevels.clear()
            if handPickedLevels is not None:
                for level in handPickedLevels:
                    if level is not None:
                        Expresso.enabledLevels.add(level)

    @staticmethod
    def setCategory(category):
        nextSet = set()
        if category is not None: nextSet.add(category.name)
        Expresso.enabledCategories = nextSet

    @staticmethod
    def setCategories(*handPickedCategories):
        nextSet = set()
        if handPickedCategories is not None:
            for category in handPickedCategories:
                if category is not None: nextSet.add(category.name)
        Expresso.enabledCategories = nextSet

    @staticmethod
    def getCurrentEventCount():
        with Expresso.counterLock: return Expresso.globalEventCounter

    @staticmethod
    def getCategories(): return frozenset(Expresso.enabledCategories)

    @staticmethod
    def getLevels(): return frozenset(Expresso.enabledLevels)

    @staticmethod
    def setTimeSource(source): Expresso.timeSource = source

    @staticmethod
    def enableApplicationTime(enable): Expresso.showApplicationTimeTag = enable

    @staticmethod
    def setBridge(outsideSystem): Expresso.externalBridge = outsideSystem

    @staticmethod
    def isExposed(category, requiredLevel):
        if category is None or requiredLevel is None: return False

        activeCategories = Expresso.enabledCategories
        if activeCategories and category.name not in activeCategories:
            return False

        activeLevels = Expresso.enabledLevels

        with Expresso.levelsLock:
            if not activeLevels: return False

            if len(activeLevels) == 1:
                activeLevel = next(iter(activeLevels))
                if activeLevel.getLevel() < requiredLevel.getLevel(): return False
            else:
                if requiredLevel not in activeLevels: return False

        return True

    @staticmethod
    def printf(*args):
        if len(args) < 3:
            raise TypeError("printf requires at least category, requiredLevel and format")

        if isinstance(args[0], ExposureCategory):
            identity = ""
            category = args[0]
            requiredLevel = args[1]
            formatString = args[2]
            formatArgs = args[3:]
        else:
            identity = args[0]
            category = args[1]
            requiredLevel = args[2]
            formatString = args[3]
            formatArgs = args[4:]

        if not Expresso.isExposed(category, requiredLevel): return

        with Expresso.counterLock:
            Expresso.globalEventCounter += 1
            currentIndex = Expresso.globalEventCounter

        if currentIndex < Expresso.minIndex or currentIndex > Expresso.maxIndex: return

        output = ""

        if Expresso.showApplicationTimeTag:
            source = Expresso.timeSource
            if source is not None:
                applicationTime = source.getTime()
                if applicationTime is not None and str(applicationTime).strip():
                    output += Expresso.DIM + "[" + str(applicationTime) + "] " + Expresso.RESET

        if Expresso.showTimestampTag:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            output += Expresso.DIM + "[" + timestamp + "] " + Expresso.RESET

        if Expresso.showElapsedTimeTag:
            elapsedMillis = (time.perf_counter() - Expresso.runtimeStart) * 1000.0
            output += Expresso.DIM + f"[+{elapsedMillis:.3f}ms] " + Expresso.RESET

        if Expresso.showIndexTag:
            output += Expresso.DIM + f"[#{currentIndex}] " + Expresso.RESET

        if Expresso.showIdentityTag and identity is not None and str(identity).strip():
            output += Expresso.DIM + f"[{identity}] " + Expresso.RESET

        if Expresso.showCategoryTag:
            output += Expresso.DIM + f"[{category.name}] " + Expresso.RESET

        if Expresso.showLevelTag:
            output += Expresso.DIM + f"[{requiredLevel.name}] " + Expresso.RESET

        if formatArgs:
            try:  output += formatString % formatArgs
            except TypeError: output += formatString.format(*formatArgs)
        else: output += formatString

        Expresso.emit(output)

    @staticmethod
    def emit(text):
        bridge = Expresso.externalBridge
        if bridge is not None:
            bridge(text)
        else:
            print(text, end="")

    @staticmethod
    def appendDiagnosticTags():
        output = ""
        if not Expresso.showDiagnosticTags: return output

        if Expresso.showApplicationTimeTag and Expresso.timeSource is not None:
            appTime = Expresso.timeSource.getTime()
            if appTime is not None and str(appTime).strip():
                output += Expresso.DIM + f"[{appTime}] " + Expresso.RESET

        if Expresso.showTimestampTag:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            output += Expresso.DIM + f"[{timestamp}] " + Expresso.RESET

        if Expresso.showElapsedTimeTag:
            elapsedMillis = (time.perf_counter() - Expresso.runtimeStart) * 1000.0
            output += Expresso.DIM + f"[+{elapsedMillis:.3f}ms] " + Expresso.RESET

        return output

    @staticmethod
    def error(formatString, *args):
        exception = None
        formattingArgs = list(args)

        if formattingArgs and isinstance(formattingArgs[-1], BaseException):
            exception = formattingArgs.pop()

        output = Expresso.appendDiagnosticTags()
        output += Expresso.errorColor + Expresso.errorPrefix + Expresso.RESET

        if formattingArgs:
            try: output += formatString % tuple(formattingArgs)
            except TypeError: output += formatString.format(*formattingArgs)
        else: 
            output += formatString

        if exception is not None:
            output += "\n"
            output += "".join(traceback.format_exception(type(exception), exception, exception.__traceback__))

        Expresso.emit(output)

    @staticmethod
    def hereAnnounce(identity=None, customColor = None, customHeader = None, label = None):
        output = Expresso.appendDiagnosticTags()
        color = customColor if customColor is not None else Expresso.hereColor
        header = customHeader if customHeader is not None else Expresso.hereHeader

        if identity is not None and str(identity).strip(): output += "[" + str(identity) + "] "

        output += color + header + Expresso.RESET

        if label is not None and str(label).strip(): output += ": " + str(label)
        output += "\n"
            
        Expresso.emit(output)


class Exposure:

    def __init__(self, identity = None): self.identity = identity

    def expose(self, category, level, formatString, *args):
        if callable(formatString):
            if not Expresso.isExposed(category, level):
                return
            Expresso.printf(self.identity, category, level, "%s", formatString())
        else:
            Expresso.printf(self.identity, category, level, formatString, *args)

    def l1(self, category, formatString, *args):
        if callable(formatString):
            if not Expresso.isExposed(category, ExposureLevel.LEVEL1): return
            Expresso.printf(self.identity, category, ExposureLevel.LEVEL1, "%s", formatString())
        else:
            Expresso.printf(self.identity, category, ExposureLevel.LEVEL1, formatString, *args)

    def l2(self, category, formatString, *args):
        if callable(formatString):
            if not Expresso.isExposed(category, ExposureLevel.LEVEL2): return
            Expresso.printf(self.identity, category, ExposureLevel.LEVEL2, "%s", formatString())
        else:
            Expresso.printf(self.identity, category, ExposureLevel.LEVEL2, formatString, *args)

    def l3(self, category, formatString, *args):
        if callable(formatString):
            if not Expresso.isExposed(category, ExposureLevel.LEVEL3): return
            Expresso.printf(self.identity, category, ExposureLevel.LEVEL3, "%s", formatString())
        else:
            Expresso.printf(self.identity, category, ExposureLevel.LEVEL3, formatString, *args)

    def l4(self, category, formatString, *args):
        if callable(formatString):
            if not Expresso.isExposed(category, ExposureLevel.LEVEL4): return
            Expresso.printf(self.identity, category, ExposureLevel.LEVEL4, "%s", formatString())
        else:
            Expresso.printf(self.identity, category, ExposureLevel.LEVEL4, formatString, *args)

    def l5(self, category, formatString, *args):
        if callable(formatString):
            if not Expresso.isExposed(category, ExposureLevel.LEVEL5): return
            Expresso.printf(self.identity, category, ExposureLevel.LEVEL5, "%s", formatString())
        else:
            Expresso.printf(self.identity, category, ExposureLevel.LEVEL5, formatString, *args)

    def nl(self, category, requiredLevel):
        Expresso.NEWLINE(category, requiredLevel)

    def lbr(self, category, requiredLevel):
        Expresso.LINEBREAK(category, requiredLevel)

    def err(self, formatString, *args):
        if self.identity is not None and str(self.identity).strip():
            Expresso.error("[" + str(self.identity) + "] " + formatString, *args)
        else:
            Expresso.error(formatString, *args)

    def here(self, label=None, customColor=None, customHeader=None):
        Expresso.hereAnnounce(identity=self.identity, customColor=customColor, customHeader=customHeader, label=label)

    def getIdentity(self):
        return self.identity