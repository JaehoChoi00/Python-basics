# With

[:arrow_left: Return to Main README](../../README.md)

> This is a full rundown of the [`With.py`](/extraPython/With.py) file

---

> **Terminal code for running**:
> ```bash
> python3 With.py
> ```

## Sections

> * [Basic Resource](#basic-resource)
> * [Multiple Resources](#multiple-resources)
> * [Threading Lock](#threading-lock)
> * [Testing](#testing)

---

## Basic Resource

***Python Syntax***

```py
def functionWithBasicWith():
    with open("example.txt", "w") as file:
        file.write("Writing data safely.")
        print("Executing code inside the indented 'with' block.")

    print("Out of indentation. The resource/file is now automatically closed!")
```

---

## Multiple Resources

***Python Syntax***

```py
def functionWithMultipleResources():
    with open("example.txt", "r") as sourceFile, open("backup.txt", "w") as backupFile:
        dataContent = sourceFile.read()
        backupFile.write(dataContent)
        print("Both files are actively open right now inside this block.")

    print("Out of indentation. Both files are completely closed!")
```

---

## Threading Lock

***Race Condition Visualized***
```txt
    Thread 1                    Thread 2                    Thread 3
        │                           │                           │
        │                           │                           │  
        ▼                           ▼                           ▼
    ┌──────────────────────────────────────────────────────────────┐
    │                    THREADING LOCK INTERFACE                  │
    │                                                              │
    │  [LOCK ACQUIRED] ◄─────── [LOCK AVAILABLE]                   │
    │        │                        │                            │
    │        ▼                        ▼                            │
    │    Thread 1                 Thread 2             Thread 3    │
    │  (Runs Code)               (Blocked)            (Blocked)    │
    │  Increments counter     Waiting in queue     Waiting in queue│
    │        │                        │                            │
    └────────┼────────────────────────┼────────────────────────────┘
             │                        │
             │ Exits 'with'           │ Wake up
             ▼                        ▼
    Releases Lock ─────────►   Acquires Lock
    (Auto-Unlock)                     │
                                      ▼
                                  Runs Code
                              Increments Counter
```

***Python Syntax***

```py
def functionWithThreadingLock(lock, sharedCounterDict):
    with lock:
        sharedCounterDict["value"] += 1
        print(f"Inside lock context. Counter safely updated to: {sharedCounterDict['value']}")

    print("Out of indentation. The lock has been automatically released!")
```

---

## Testing

***Python Syntax***

```py
print("\n[The 'with' Syntax]")
print()

functionWithBasicWith()
print()

functionWithMultipleResources()
print()

myLock = threading.Lock()
myCounter = {"value": 0}

functionWithThreadingLock(myLock, myCounter)
print()

if os.path.exists("example.txt"): os.remove("example.txt")
if os.path.exists("backup.txt"): os.remove("backup.txt")
```

***Output***

```txt
[The 'with' Syntax]

Executing code inside the indented 'with' block.
Out of indentation. The resource/file is now automatically closed!

Both files are actively open right now inside this block.
Out of indentation. Both files are completely closed!

Inside lock context. Counter safely updated to: 1
Out of indentation. The lock has been automatically released!
```

<FollowUp>
Let me know if you want to create a similar visual reference guide for any other Python concurrency features, such as **threading.Thread loops** or **asyncio event cycles**!
</FollowUp>
