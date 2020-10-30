+++
title = "Variables and Types"
date = 2020-08-29T16:53:07-07:00
weight = 5
+++

## Open The REPL

Learn about variables by typing along in the Python REPL.

{{% notice tip %}}
Open the REPL from VS Code by opening the command palette (`Ctrl + Shift + P` on Windows, or `Cmd + Shift + P` on Mac) and selecting Python: Start REPL
{{% /notice %}}

Any Python code that starts with the `>>>` symbols indicates that it was typed into a REPL.

You can then use <code>Ctrl + &#96;</code> (backtick) to open and close the VS Code terminal on Mac, or `Ctrl + '` (single quote) on Windows. You won't lose your work in the REPL unless you close VS Code.

{{% notice info %}}
If you'd like to save the contents of your REPL as class goes on, you can right click, select all, and paste it into a new file.
{{% /notice %}}

## Variables

#### Values and Names

Variables in Python allow us to store information and give it a label that we can use to retrieve that information later.

We assign _values_ to _variables_ by putting the _value_ to the right of an equal sign.

#### Python is a Dynamic Language

Because Python is a *dynamic* language, you'll notice we don't need to declare the type of the variables before we store data in them.

That means that this is valid Python code:

```python
>>> x = 42
```

Unlike typed languages, the type of what's contained in Python variables can change at any time.

For example, the below is perfectly valid Python code:

```python
>>> x = 42
>>> x = "hello"
```

Here, the value of the variable `x` changed from a number to a string.

Because Python is a dynamic language, you don't have type hints to explain what's stored inside a variable while reading code. You should do your best to name your variables in a way that describes what is stored in them.

It's ok to be _verbose_. For example, `n` is a poor variable name, while `number` is a better one. If you're storing a collection of items, name your variable as a plural, like `numbers`.

{{% notice note %}}
Learn more about great naming practices for dynamic types by watching this 30-minute talk [Dynamic Types Meet Smart Conventions](https://www.youtube.com/watch?v=YklKUuDpX5c).
{{% /notice %}}

#### Naming Variables

Convention says that variables should be named in lowercase and start with a letter or an underscore (not a number). Whole words should be separated by underscores. This is called snake case.

Some names will result in a syntax error, like if you try to name your variables `and`, `if`, `True`, or `False`. That's because Python uses these names for program control structure. You can't start your variable name with a digit, although your variable name can end in a digit. Your variable name also can't contain special characters, such as `!`,  `@`,  `#`, `$`,  `%`.

Other names won't result in a syntax error, but can cause weird bugs that are hard to diagnose and troubleshoot. You don't want to name your variables the same as the *types* that we'll be working with. For example **don't** name your variables `int`, `list`, `dict`, etc.

If you notice your program behaving oddly and you can't find the source of the bug, double check the list of [built-in functions](https://docs.python.org/3/library/functions.html) and [built-in types](https://docs.python.org/3/library/stdtypes.html) to make sure that your variable names don't conflict.

{{% notice warning %}}
💣 Python will let you override built-in methods and types without a warning so don't name your Python variables things like `list`, `str`, or `int`.
{{% /notice %}}

{{% notice note %}}
If you want to learn more about Python naming conventions look at [PEP8](https://www.python.org/dev/peps/pep-0008/#naming-conventions) during a break.
{{% /notice %}}

### No-Value, `None`, or Null Value

There's a special type in Python that signifies no value at all. In other languages, it might be called Null. In Python, it's called `None`.

If you try to examine a variable on the REPL that's been set to `None`, you won't see any output. We'll talk more about the `None` type later in the class.

```python
>>> x = None
>>> x
```

## Using `type()`, `dir()`, and `help()` in the REPL

There are three very useful methods we can use in the REPL to help us understand our Python programs.

### `type()`

Python has a very easy way of determining the type of something: with the `type()` function.

Just pass any object into the `type()` method:

```python
>>> num = 42
>>> type(num)
<class 'int'>
```

For example, in the REPL, let's make a new variable `name`, and check its `type`.

```python
>>> name = "Nina"
>>> type(name)
<class 'str'>
```

We'll see that the type is `str`, Python's version of a string. Now that we know this object's type, we can
pass the type into other methods.

### `dir()`

`dir()` stands for directory. If we check the type of `str` (notice, no quotes here) in the REPL, we'll see all the methods available on strings in Python. We'll use some of these methods later in the day.

```Python
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

### `help()` 

The last useful method is `help()`. You can pass a type, method, or other object to `help()` to instantly see available documentation about the method, the parameters it expects, and what it returns.

Let's try this in the REPL, and look up the documentation for the `isupper` method in String. We access it with the period symbol (`.`). This is called dot-notation.

```python
>>> help(str.isupper)
```

Will show:

```text
isupper(self, /)
    Return True if the string is an uppercase string, False otherwise.

    A string is uppercase if all cased characters in the string are uppercase and
    there is at least one cased character in the string.
```

{{% notice note %}}
Press the 'q' key to exit this screen.
{{% /notice %}}

Keep note of these three helpful methods; you'll be using them regularly throughout the class.