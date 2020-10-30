+++
title = "Running .py files"
date = 2020-08-29T17:00:26-07:00
weight = 1
+++


### Creating Python Files with the `*.py` extension

You know a file is a Python program when it ends with a `.py` extension.

#### Naming Tips

{{% notice tip %}}
Just like with formatting, Python's [PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/#package-and-module-names) give us a few helpful tips about how to name our Python program files.
{{% /notice %}}

ℹ️ In Python:

1. Filenames should be ***all lowercase**
1. Words should be separated with **underscores `_`**
1. Filenames should be **short**

✅ Some good example filenames:

- `apis.py`
- `exceptions.py`
- `personal_blog.py`

⛔️ Some bad example filenames:

- `MYFILE.PY`
- `CamelCaseFile.py`
- `really_long_over_descriptive_project_file_name.py`


#### What are `*.pyc` files?

{{% notice note %}}
For optimization and other reasons, Python code can be compiled to intermediary `.pyc` files. The good news is you don't have to worry about them. The bad news is, very occasionally stale versions of these compiled files can cause problems. To safely delete them from the current project directory, run `find . -name "*.pyc" -delete` (on linux or macOS).
{{% /notice %}}

#### `git` tip: use a `.gitignore` for Python

If you use `git` for source control, you'll want to make sure that these compiled `*.pyc` files are ignored and not added to your repository.

The best way to do this is to [add the standard `.gitignore` file for Python](https://github.com/github/gitignore/blob/master/Python.gitignore) to your project.


### Running Python Files From VS Code

Running Python files from VS Code is really quick and easy.

#### Creating New Python Files

To create a new file in VS Code, hit `Ctrl + N` on Windows and Linux, and `Cmd + N` on macOS.

This will open a new file. Next, save the file with a `.py` extension.

{{% notice info %}}
Create a new simple Python program in a file called `hello.py` in our `pyworkshop` directory with the following contents:
{{% /notice %}}

```python
# in file: hello.py
greetings = ["Hello", "Bonjour", "Hola"]

for greeting in greetings:
    print(f"{greeting}, World!")
```

#### Opening The VS Code Terminal Window

Next, you'll need to open your terminal if you don't have it open already. The quick keyboard shortcut to do that is <code>Ctrl - &#96;</code>

{{% notice note %}}
If you already had your Python REPL open, you'll need to select a terminal with a shell in it (generally, the one labeled with `1:`).
{{% /notice %}}

#### Running The File

Once you've opened your `hello.py` file and selected your new terminal window, open the VS Code command palette.

{{% notice note %}}
Open the command palette with `Ctrl+Shift+P` on Windows and Linux, and `Cmd + Shift + P` on macOS.
{{% /notice %}}

Select Python: Run Python File in Terminal

You should see:

```bash
Hello, World!
Bonjour, World!
Hola, World!
```

How easy was that? 🎉

### Running Python Files From a Non-VS Code Terminal

If you want to run a Python file without using the command palette, just open your terminal of choice, `cd` into the directory with your code, and type in the command `python` followed by a space, and the name of your Python program. Don't forget to activate your virtual environment like we did in the Environment Setup section.

```bash
(env) $ python hello.py
Hello, World!
Bonjour, World!
Hola, World!
```

This also works in the VS Code terminal.

## Printing Tips

One of the nice things about the REPL is we can quickly and easily see the contents of our variables, just by typing their name and pressing enter. Unfortunately, running code from Python files doesn't do quite the same thing.

In a file named `name.py`:

```python
# file name.py
name = "Nina"
name
```

Output:

```bash
(env) $ python name.py
```

*Notice, there was no output.*

Now, in a file named `print_name.py`:
```python
# file print_name.py
name = "Nina"
print(name)
```

Output:
```bash
(env) $ python name.py
Nina
```

Hooray! Now we see some output. 🎉

{{% notice tip %}}
If you want to see any output from your Python programs, you'll need to use `print()`.
{{% /notice %}}

### Debugging Your Code With `print()`

As your Python programs become more complicated, you'll want to do some basic debugging to figure out what's going on under the hood. For beginners, using `print()` is a great way to accomplish that goal.

{{% notice note %}}
If you write Python code on a team or plan on sharing it, it's a good idea to *remove* your debugging `print()`s before you share your code with others.
{{% /notice %}}

In a Python file named `mystery.py`:

```python
def mystery():
    num = 10 * 3

    if num == 10:
        print("Num was equal to 10")
        num = num * 10
    if num == 20:
        print("Num was equal to 20")
        num = num * 20
    if num == 30:
        print("Num was equal to 30")
        num = num * 30

    print(f"Value of returned num is: {num}")
    return num

mystery()
```

We'll see the output:

```python
Num was equal to 30
Value of returned num is: 900
```

{{% notice tip %}}
Tip: As you continue your Python journey, try using a debugger, like the built-in `pdb` instead of the `print()` function to really dive into what your code is doing under the hood.
{{% /notice %}}


### Output Formatting Tips

If your Python program will have terminal output, you can use these tips to make it a little nicer.

#### Use new lines and tabs

Use control characters in your string to change how your output is represented.

* `\n` for new line
* `\t` for tab

In `formatting_example.py`:

```python
# Use \n to add a new line, before, in the middle of, or after a string.
print("\nExtra New Line Before")
print("One Print\nTwo New Lines!")
print("Extra New Line After\n")

# Use \t to add a tab.
print("\t Here's some tabbed output.")

# Or, combine both!
print("\nOne Print\n\tOne Tab")
```

Output running: `python3 formatting_example.py`.

```text
Extra New Line Before
One Print
Two New Lines!
Extra New Line After

         Here's some tabbed output.

One Print
        One Tab
```

#### Pretty Printing with `pprint`

When printing large data structures like long lists or big dictionaries, they come out on one line. It's a bit hard to read.

If you want a little bit of extra formatting, like having each element of a long list on a new line, you can use the included `pprint` module (stands for pretty print) in your files or in the REPL.

```python
>>> long_list = list(range(23))

>>> print(long_list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

>>> from pprint import pprint
>>> pprint(long_list)
[0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 22]
```

{{% notice tip %}}
This will become more useful as your Python programs become more complex.
{{% /notice %}}