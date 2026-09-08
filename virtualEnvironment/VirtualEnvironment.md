# The Virtual Environment

[:arrow_left: Return to Main README](../README.md)

:arrow_right: [Link to **Virtual Environment** Learning Resource](https://docs.python.org/3/library/venv.html)

> This is an introduction to isolated Python environments.

## Sections

> * [`Tools`](#tools)
>   * [`Venv`](#venv)
>   * [`Virtualenv`](#virtualenv)
> * [`Creating`](#creating)
> * [`Recreating the Environment`](#recreating-the-environment)
> * [`Activating`](#activating)
> * [`Deactivating`](#deactivating)
> * [`Installing Packages`](#installing-packages)
> * [`Dependencies`](#dependencies)
> * [`Project Structure`](#project-structure)
> * [`pyproject.toml`](#pyprojecttoml)
> * [`Building`](#building)
> * [`Testing`](#testing)

---

### [Tools](#sections)

* `venv` <-- This is my focus.

* [`virtualenv`](https://packaging.python.org/en/latest/key_projects/#virtualenv)

---

### [Venv](#sections)

***Syntax: Bash***

```bash
python -m venv venv
```

Creates an isolated Python environment inside the `venv` directory.

***Syntax: Result***

```text
venv/
├── bin/
├── include/
├── lib/
└── pyvenv.cfg
```

---

### [Creating](#sections)

***Syntax: Bash***

```bash
python -m venv venv
```

`python` selects Python.

`-m venv` look at the **Module** named **venv** and **run it**.

`venv` is the environment directory.

---

### [Recreating the Environment](#sections)

```py
python -m venv venv

source venv/bin/activate

python -m pip install -r requirements.txt

Creates a new environment and restores the project's dependencies
```

### [Activating](#sections)

***Syntax: Bash***

```bash
source venv/bin/activate
```

***Syntax: Result***

```text
(venv) $
```

The terminal is now using the virtual environment.

---

### [Deactivating](#sections)

***Syntax: Bash***

```bash
deactivate
```

Returns the terminal to the previous Python environment.

---

### [Installing Packages](#sections)

***Syntax: Bash***

```bash
python -m pip install packageName
```

Installs a package into the active virtual environment.

---

### [Dependencies](#sections)

***Syntax: Bash***

```bash
python -m pip freeze > requirements.txt
```
Creates a list of installed packages and their versions.

**Or**

```bash
python -m pip install pipreqs
pipreqs /path/to/your/project
```

generates a clean requirements.txt file containing only the packages your code actually uses.


***Syntax: Bash***

```bash
python -m pip install -r requirements.txt
```

Installs the listed dependencies.

---

### [Project Structure](#sections)

***Syntax: Result***

```text
project/
├── venv/
├── src/
│   └── package/
├── tests/
├── README.md
├── LICENSE
└── pyproject.toml
```

`venv/` → isolated environment

`src/` → source code

`tests/` → tests

`pyproject.toml` → project configuration

---

### [pyproject.toml](#sections)

***Syntax: TOML***

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

Defines how the Python project is built.

---

### [Building](#sections)

***Syntax: Bash***

```bash
python -m build
```

Builds distributable package files.

---

### [Testing](#sections)

***Syntax: Bash***

```bash
python -m pip install -e .
```

Installs the current project in editable mode into the active environment so local code updates register instantly.

```bash
python -m pip show packageName
```

Displays information about the installed package.

***Python Code***

> This is outside the venv folder, but within the folder the venv is inside

```py
import os
from google import genai

client = genai.Client()
print("Gemini AI Chatbot Initialized. Type 'end' to exit.\n")
chat = client.chats.create(model="gemini-3.6-flash")

while True:
    user_input = input("User: ")
    if user_input.lower() == 'end':
        break

    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}\n")

```

***Example***

```bash
python -m pip install google-genai
export GEMINI_API_KEY="APIKEY"
python GoogleAITest.py
```

***Trackign where google-genai is saved***

```txt
project/
├── venv/
    └── lib/ <- [In Here]
```

***Result***

```txt
User: Hello!

Gemini: Greeintgs! How can I help you today?

User: _
```

---

### [Ignoring the Environment](#sections)

***Python Syntax***

```.gitignore
venv/
```

Add venv/ to .gitignore.

The virtual environment contains installed packages and environment-specific files.

It should normally not be committed to Git.
