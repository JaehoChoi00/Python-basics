import os
import threading

def functionWithBasicWith():
    with open("example.txt", "w") as file:                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        file.write("Writing data safely.")
        print("Executing code inside the indented 'with' block.")
    
    print("Out of indentation. The resource/file is now automatically closed!")


def functionWithMultipleResources():
    # Demonstrates managing two separate resources at the same time using a comma
    with open("example.txt", "r") as sourceFile, open("backup.txt", "w") as backupFile:
        dataContent = sourceFile.read()
        backupFile.write(dataContent)
        print("Both files are actively open right now inside this block.")

    print("Out of indentation. Both files are completely closed!")

def functionWithThreadingLock(lock, sharedCounterDict):
    # Demonstrates managing a thread lock instead of a file resource
    # 'with' automatically calls lock.acquire() at the start and lock.release() at the end
    with lock:
        sharedCounterDict["value"] += 1
        print(f"Inside lock context. Counter safely updated to: {sharedCounterDict['value']}")
        
    print("Out of indentation. The lock has been automatically released!")


print("\n[The 'with' Syntax]")
print() # NEWLINE

# Basic Single Resource Management
functionWithBasicWith()
print() # NEWLINE

# Advanced Multi-Resource Management (Chained with a comma)
functionWithMultipleResources()
print()

# Threading Lock Resource Management
myLock = threading.Lock()
myCounter = {"value": 0}
functionWithThreadingLock(myLock, myCounter)
print() # NEWLINE

if os.path.exists("example.txt"): os.remove("example.txt")
if os.path.exists("backup.txt"): os.remove("backup.txt")

