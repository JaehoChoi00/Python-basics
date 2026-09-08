# Pip

[:arrow_left: Return to Main README](../README.md)

> [Pip](<https://pip.pypa.io/en/stable/#:~:text=Pip%20is%20the%20package%20installer%20for%20Python>) is the [standard package installer for python](<https://packaging.python.org/en/latest/guides/tool-recommendations/#:~:text=pip%20is%20the%20standard%20tool%20to%20install%20packages%20from%20PyPI>).  
> 
> A tool to install packages from [PyPI (Python Package Index)](<https://packaging.python.org/en/latest/glossary/#term-Python-Package-Index-PyPI:~:text=Discourse%20forum.-,Python%20Package%20Index%20(PyPI),-%C2%B6>).

:arrow_right: [Link to **Pip** Documentation](https://pip.pypa.io/en/stable/)

## Sections

> * [The Prologue](#the-prologue)
> * [Using Pip](#using-pip)
 
---

### [The Prologue](#sections)

#### The Setup

> TLDR (Too Long; Didn't Read)  
>
> Installation for all OS is the same **EXCEPT**:
> 
> * **Linux / macOS**: The command is `python` (or `python3`).
>     * **Mac / Linux** connect directly to the software, where `python3` explicitly runs the modern version (while `python` usually runs the outdated Python 2).
> * **Windows**: The command is `py`.
>     * **Windows** uses the Python Launcher (`py`), which actively maps out every version of Python installed on the machine.
>     * It acts as an intelligent router, intercepting the `py` command and forwarding it to the exact version requested (e.g., `py -3.12`), preventing global path conflicts.
>
> **FYI** (For Your Information)  
> * My Computer is macOS

### [Using Pip](#sections)

**Upgrading Syntax: Bash**

```bash
python3 -m pip install --upgrade pip
```

**Installing Syntax: Bash**

```bash
python3 -m pip install packageName
```

**Uninstalling Syntax: Bash**

```bash
python3 -m pip uninstall packageName
```